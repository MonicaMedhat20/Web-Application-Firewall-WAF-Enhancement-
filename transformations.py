import re
import base64
import html
import json
import hashlib
import urllib.parse

class Waf_Transforms:
    def base64_decode(self, value):
        return base64.b64decode(value).decode('utf-8')

    def cmd_line(self, value):
        return re.sub(r'\s+', ' ', re.sub(r'\s+(?=[\/\(])', '', re.sub(r'[\^\'"\\,;]', '', value.lower())))

# Example usage:
waf_transforms = Waf_Transforms()

# Base64 Decode
base64_decoded = waf_transforms.base64_decode("SGVsbG8sIFdvcmxkIQ==")
print("Base64 Decoded:", base64_decoded)

# CMD Line
cmd_line_transformed = waf_transforms.cmd_line("Hello, World!; ls -l /")
print("CMD Line Transformed:", cmd_line_transformed)


class Waf_Transforms:
    def sql_hex_decode(self, value):
        return re.sub(
            r'0x[a-f0-9]+',
            lambda match: bytes.fromhex(match.group(0)[2:]).decode('utf-8'),
            value
        )

    def base64_encode(self, value):
        return base64.b64encode(value.encode('utf-8')).decode('utf-8')

    def compress_whitespace(self, value):
        return re.sub(r'\s+', ' ', value)

    def hex_encode(self, value):
        return value.encode('utf-8').hex()

    def hex_decode(self, value):
        return bytes.fromhex(value).decode('utf-8')

    def html_entity_decode(self, value):
        return html.unescape(value)

# Example usage:
waf_transforms = Waf_Transforms()

# SQL Hex Decode
sql_hex_decoded = waf_transforms.sql_hex_decode("0x414243")
print("SQL Hex Decoded:", sql_hex_decoded)

# Base64 Encode
base64_encoded = waf_transforms.base64_encode("Hello, World!")
print("Base64 Encoded:", base64_encoded)

# Compress Whitespace
compressed_whitespace = waf_transforms.compress_whitespace("   Hello,   World!   ")
print("Compressed Whitespace:", compressed_whitespace)

# Hex Encode
hex_encoded = waf_transforms.hex_encode("ABC")
print("Hex Encoded:", hex_encoded)

# Hex Decode
hex_decoded = waf_transforms.hex_decode("414243")
print("Hex Decoded:", hex_decoded)

# HTML Entity Decode
html_entity_decoded = waf_transforms.html_entity_decode("&lt;div&gt;Hello, World!&lt;/div&gt;")
print("HTML Entity Decoded:", html_entity_decoded)





class Waf_Transforms:
    def length(self, value):
        return len(value)

    def lowercase(self, value):
        return value.lower()

    def md5(self, value):
        return hashlib.md5(value.encode('utf-8')).digest()

    def normalize_path(self, value):
        parts = value.split('/')
        i = 0
        while i < len(parts):
            if parts[i] == '..':
                if i > 0 and parts[i - 1] not in ('', '..'):
                    del parts[i - 1:i + 1]
                    i -= 1
                    continue
            elif parts[i] == '.':
                del parts[i]
                continue
            i += 1
        return '/'.join(parts)

    def normalize_path_win(self, value):
        return self.normalize_path(value.replace('\\', '/'))

    def remove_nulls(self, value):
        return value.replace('\x00', '')

# Example usage:
waf_transforms = Waf_Transforms()

# Test the functions with sample input
print("Length:", waf_transforms.length("Hello, World!"))
print("Lowercase:", waf_transforms.lowercase("Hello, World!"))
print("MD5:", waf_transforms.md5("Hello, World!"))
print("Normalize Path:", waf_transforms.normalize_path("/path/to/some/../file"))
print("Normalize Path Win:", waf_transforms.normalize_path_win("C:\\path\\to\\file"))
print("Remove Nulls:", waf_transforms.remove_nulls("Hello\x00World"))






class Waf_Transforms:
    def remove_whitespace(self, value):
        return re.sub(r'\s', '', value)

    def replace_comments(self, value):
        value = re.sub(r'/\*.*?\*/|/\*.*?$', ' ', value, flags=re.DOTALL)
        return value.split('/*', 1)[0]

    def remove_comments_char(self, value):
        return re.sub(r'/\*|\*/|--|#|//', '', value)

    def replace_nulls(self, value):
        return value.replace('\x00', ' ')

    def url_decode(self, value):
        return urllib.parse.unquote(value)

    def url_decode_uni(self, value):
        print('JETPACKWAF TRANSFORM NOT IMPLEMENTED: urlDecodeUni')
        return value

    def js_decode(self, value):
        print('JETPACKWAF TRANSFORM NOT IMPLEMENTED: jsDecode')
        return value

    def uppercase(self, value):
        return value.upper()

    def sha1(self, value):
        return hashlib.sha1(value.encode('utf-8')).digest()

    def trim_left(self, value):
        return value.lstrip()

    def trim_right(self, value):
        return value.rstrip()

    def trim(self, value):
        return value.strip()

    def utf8_to_unicode(self, value):
        return re.sub(r'\\u(?=[a-f0-9]{4})', '%u', json.dumps(value, ensure_ascii=False))[1:-1]

# Example usage:
waf_transforms = Waf_Transforms()

# Test the functions with sample input
print("Remove Whitespace:", waf_transforms.remove_whitespace("  Hello,   World!  "))
print("Replace Comments:", waf_transforms.replace_comments("/* Comment */ Hello, World!"))
print("Remove Comments Char:", waf_transforms.remove_comments_char("# Comment\nHello, World!"))
print("Replace Nulls:", waf_transforms.replace_nulls("Hello\x00World"))
print("URL Decode:", waf_transforms.url_decode("Hello%20World%21"))
print("URL Decode Uni:", waf_transforms.url_decode_uni("Hello%20World%21"))
print("JS Decode:", waf_transforms.js_decode('{"key": "value"}'))
print("Uppercase:", waf_transforms.uppercase("Hello, World!"))
print("SHA1:", waf_transforms.sha1("Hello, World!"))
print("Trim Left:", waf_transforms.trim_left("   Hello, World!   "))
print("Trim Right:", waf_transforms.trim_right("   Hello, World!   "))
print("Trim:", waf_transforms.trim("   Hello, World!   "))
print("UTF-8 to Unicode:", waf_transforms.utf8_to_unicode("Hello, World!"))
