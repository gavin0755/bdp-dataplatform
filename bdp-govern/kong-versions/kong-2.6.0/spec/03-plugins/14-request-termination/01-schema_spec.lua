local schema_def = require "kong.plugins.request-termination.schema"
local v = require("spec.helpers").validate_plugin_config_schema

describe("Plugin: request-termination (schema)", function()
  it("should accept a valid status_code", function()
    assert(v({status_code = 404}, schema_def))
  end)
  it("should accept a valid message", function()
    assert(v({message = "Not found"}, schema_def))
  end)
  it("should accept a valid content_type", function()
    assert(v({content_type = "text/html",body = "<body><h1>Not found</h1>"}, schema_def))
  end)
  it("should accept a valid body", function()
    assert(v({body = "<body><h1>Not found</h1>"}, schema_def))
  end)
  it("should accept trigger", function()
    assert(v({ echo = true, trigger = "header_name" }, schema_def))
  end)

  describe("errors", function()
    it("status_code should only accept numbers", function()
      local ok, err = v({status_code = "abcd"}, schema_def)
      assert.falsy(ok)
      assert.same("expected an integer", err.config.status_code)
    end)
    it("status_code < 100", function()
      local ok, err = v({status_code = 99}, schema_def)
      assert.falsy(ok)
      assert.same("value should be between 100 and 599", err.config.status_code)
    end)
    it("status_code > 599", function()
      local ok,err = v({status_code = 600}, schema_def)
      assert.falsy(ok)
      assert.same("value should be between 100 and 599", err.config.status_code)
    end)
    it("#message with body", function()
      local ok, err = v({message = "error", body = "test"}, schema_def)
      assert.falsy(ok)
      assert.same("message cannot be used with content_type or body", err.config)
    end)
    it("message with body and content_type", function()
      local ok, err = v({message = "error", content_type="text/html", body = "test"}, schema_def)
      assert.falsy(ok)
      assert.same("message cannot be used with content_type or body", err.config)
    end)
    it("message with content_type", function()
      local ok, err = v({message = "error", content_type="text/html"}, schema_def)
      assert.falsy(ok)
      assert.same("message cannot be used with content_type or body", err.config)
    end)
    it("content_type without body", function()
      local ok, err = v({content_type="text/html"}, schema_def)
      assert.falsy(ok)
      assert.same("content_type requires a body", err.config)
    end)
    it("echo with body & content_type", function()
      local ok, err = v({echo = true, content_type = "text/html",body = "<body><h1>Not found</h1>"}, schema_def)
      assert.falsy(ok)
      assert.same("echo cannot be used with content_type and body", err.config)
    end)
  end)
end)