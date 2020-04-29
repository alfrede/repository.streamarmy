# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgcmUNCmltcG9ydCB4Ym1jDQppbXBvcnQgeGJtY2d1aQ0KaW1wb3J0IHRpbWUNCmZyb20gcmFuZG9tIGltcG9ydCByYW5kaW50DQpkaWFsb2cgPSB4Ym1jZ3VpLkRpYWxvZygpDQp1YSA9ICgnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXaW42NDsgeDY0KSAnDQogICAgICAnQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgJw0KICAgICAgJ0Nocm9tZS82NS4wLjMzMjUuMTgxIFNhZmFyaS81MzcuMzYnKQ0KY2xhc3MgU2NyYXBlcjoNCglkZWYgX19pbml0X18oc2VsZik6DQoJCXNlbGYuQmFzZSA9ICdodHRwczovL3Bhc3RlYmluLmNvbS9yYXcveThuWXVVUFAnDQoJCXNlbGYuU2VhcmNoID0gKCcvJXMtd2F0Y2gtb25saW5lLycpDQoJCXNlbGYubGlua3MgPSBbXQ0KDQoJZGVmIEluZGV4KHNlbGYsdHlwZSwgdGVybSx5ZWFyLGltZGIsdG9ycmVudHMpOg0KCQlpZiAnVFYnIGluIHR5cGU6IHJldHVybiBGYWxzZQ0KCQlsaW5rID0gcmVxdWVzdHMuZ2V0KHNlbGYuQmFzZSwgaGVhZGVycz17IlVzZXItQWdlbnQiOnVhfSkuY29udGVudA0KCQltYXRjaGVzID0gcmUuZmluZGFsbCgnPGxpc3Q+KC4qPyk8L2xpc3Q+JyxsaW5rLGZsYWdzPXJlLkRPVEFMTCkNCgkJZm9yIGNvbnRlbnQgaW4gbWF0Y2hlczo'
love = 'APtxWPJyzVPp8oJ92nJImCvptnJ4tL29hqTIhqQbAPtxWPDywnTIwn3IloPN9VUWyYzMcozEuoTjbWmkgo3McMKZ+XP4dClx8Y21iqzyypm4aYTAioaEyoaDfMzkuM3Z9pzHhER9HDHkZXD0XPDxWPJMipvOfnJ5eplOcovOwnTIwn3IloQbAPtxWPDxWp2IupzAbL29hqTIhqPN9VUWypKIyp3EmYzqyqPufnJ5eplkbMJSxMKWmCKfvIKAypv1OM2IhqPV6qJS9XF5wo250MJ50QDbWPDxWPJkcp3EmVQ0tpzHhMzyhMTSfoPtaCTAioaEyoaD+XP4dClx8Y2AioaEyoaD+WlkmMJSlL2uwo250MJ50YTMfLJqmCKWyYxECIRSZGPxAPtxWPDxWMz9lVTI4pTShMPOcovOfnKA0pmbAPtxWPDxWPJyzVUEypz0hoT93MKVbXFOcovOyrUOuozDhoT93MKVbXGbAPtxWPDxWPDy0nKEfMFN9VUWyYzMcozEuoTjbWmk0nKEfMG4bYvb/XGjiqTy0oTH+WlkyrUOuozDfMzkuM3Z9pzHhER9HDHkZXIfjKD0XPDxWPDxWPJkcozftCFOlMF5znJ5xLJkfXPp8oTyhnm4bYvb/XGjioTyhnm4aYTI4pTShMPkzoTSapm1lMF5RG1EOGRjcQDbWPDxWPDxWnJLtoTyhnlN+VQRtBt0XPDxWPDxWPDyzo3VtoTyhn3ZtnJ4toTyhnmbAPtxWPDxWPDxWPJyzVPq0pzScoTIlWlOcovOfnJ5epl5fo3qypvtcBvOwo250nJ51MD0XPDxWPDxWPDxWnJLtW3IbMPptnJ4tqTy0oTHhoT93MKVbXGbAPtxWPDxWPDxWPDyhLJ'
god = '1lID0gJ05lbWVzaXNBaW8gQ29udGVudCB8IDRLIHwgJyArIHRpdGxlDQoJCQkJCQkJCQkJcXVhbGl0eSA9ICc1Jw0KCQkJCQkJCQkJZWxpZiAnNGsnIGluIHRpdGxlLmxvd2VyKCk6DQoJCQkJCQkJCQkJbmFtZSA9ICdOZW1lc2lzQWlvIENvbnRlbnQgfCA0SyB8ICcgKyB0aXRsZQ0KCQkJCQkJCQkJCXF1YWxpdHkgPSAnNScNCgkJCQkJCQkJCWVsaWYgJzEwODAnIGluIHRpdGxlLmxvd2VyKCk6DQoJCQkJCQkJCQkJbmFtZSA9ICdOZW1lc2lzQWlvIENvbnRlbnQgfCAxMDgwIHwgJyArIHRpdGxlDQoJCQkJCQkJCQkJcXVhbGl0eSA9ICc2Jw0KCQkJCQkJCQkJZWxpZiAnNzIwJyBpbiB0aXRsZS5sb3dlcigpOg0KCQkJCQkJCQkJCW5hbWUgPSAnTmVtZXNpc0FpbyBDb250ZW50IHwgSEQgfCAnICsgdGl0bGUNCgkJCQkJCQkJCQlxdWFsaXR5ID0gJzcnDQoJCQkJCQkJCQllbHNlOg0KCQkJCQkJCQkJCW5hbWUgPSAnTmVtZXNpc0FpbyBDb250ZW50IHwgU0QgfCAnICsgdGl0bGUNCgkJCQkJCQkJCQlxdWFsaXR5ID0gJzgnDQoJCQkJCQkJCQlzZWxmLmxpbmtzLmFwcGVuZCh7J3RpdGxlJzogbmFtZSwgJ3VybCc6IGxpbmtzICwgJ3F1YWxpdHknIDogcXVhbGl0eX0pDQoJCQkJCQkJZWxzZToNCgkJCQkJCQkJaWYgJ3RyYWlsZXInIGluIGxpbmsubG93ZXIoKTogY29udGlud'
destiny = 'JHAPtxWPDxWPDxWnJLtW3IbMPptnJ4tqTy0oTHhoT93MKVbXGbAPtxWPDxWPDxWPJ5uoJHtCFNaGzIgMKAcp0ScolOQo250MJ50VUjtARftsPNaVPftqTy0oTHAPtxWPDxWPDxWPKS1LJkcqUxtCFNaZPpAPtxWPDxWPDxWMJkcMvNaATfaVTyhVUEcqTkyYzkiq2IlXPx6QDbWPDxWPDxWPDyhLJ1yVQ0tW05yoJImnKAOnJ8tD29hqTIhqPO8VQEYVUjtWlNeVUEcqTkyQDbWPDxWPDxWPDykqJSfnKE5VQ0tWmNaQDbWPDxWPDxWPJIfnJLtWmRjBQNaVTyhVUEcqTkyYzkiq2IlXPx6QDbWPDxWPDxWPDyhLJ1yVQ0tW05yoJImnKAOnJ8tD29hqTIhqPO8VQRjBQNtsPNaVPftqTy0oTHAPtxWPDxWPDxWPKS1LJkcqUxtCFNaZFpAPtxWPDxWPDxWMJkcMvNaAmVjWlOcovO0nKEfMF5fo3qypvtcBt0XPDxWPDxWPDxWozSgMFN9VPqBMJ1yp2ymDJyiVRAioaEyoaDtsPOVEPO8VPptXlO0nKEfMD0XPDxWPDxWPDxWpKIuoTy0rFN9VPplWj0XPDxWPDxWPDyyoUAyBt0XPDxWPDxWPDxWozSgMFN9VPqBMJ1yp2ymDJyiVRAioaEyoaDtsPOGEPO8VPptXlO0nKEfMD0XPDxWPDxWPDxWpKIuoTy0rFN9VPpmWj0XPDxWPDxWPDymMJkzYzkcozgmYzSjpTIhMPu7W3EcqTkyWmbtozSgMFjtW3IloPp6VTkcozgmVPjtW3S1LJkcqUxaVQbtpKIuoTy0rK0cQDbWPKWyqUIlovOmMJkzYzkcozgmQDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))