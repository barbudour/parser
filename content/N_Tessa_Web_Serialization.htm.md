# Tessa.Web.Serialization - пространство имён
API сериализации, используемое при взаимодействии с контроллерами desktop-
клиента, в т.ч. MIME-тип applications/x-tessa.
##  __Классы
[RawRequestBodyFormatter](T_Tessa_Web_Serialization_RawRequestBodyFormatter.htm)|
Formatter that allows content of type text/plain and application/octet stream
or no content type to be parsed to raw data. Allows for a single input
parameter in the form of: public string RawString([FromBody] string data)
public byte[] RawData([FromBody] byte[] data)  
---|---  
[ResponseContentTypeHelper](T_Tessa_Web_Serialization_ResponseContentTypeHelper.htm)|  
[TessaBsonInputFormatter](T_Tessa_Web_Serialization_TessaBsonInputFormatter.htm)|  
[TessaBsonOutputFormatter](T_Tessa_Web_Serialization_TessaBsonOutputFormatter.htm)|  
[TessaBsonResult](T_Tessa_Web_Serialization_TessaBsonResult.htm)|  
[TessaBsonResultExecutor](T_Tessa_Web_Serialization_TessaBsonResultExecutor.htm)|  
[TessaJsonInputFormatter](T_Tessa_Web_Serialization_TessaJsonInputFormatter.htm)|  
[TessaJsonOutputFormatter](T_Tessa_Web_Serialization_TessaJsonOutputFormatter.htm)|  
[TessaJsonResultExecutor](T_Tessa_Web_Serialization_TessaJsonResultExecutor.htm)|  
[TessaNewtonsoftDataContractResolver](T_Tessa_Web_Serialization_TessaNewtonsoftDataContractResolver.htm)|  
[TypedJsonBinder](T_Tessa_Web_Serialization_TypedJsonBinder.htm)|  
[TypedJsonBodyAttribute](T_Tessa_Web_Serialization_TypedJsonBodyAttribute.htm)|  
[TypedJsonResult](T_Tessa_Web_Serialization_TypedJsonResult.htm)|  
[TypedJsonSerializerObjectPolicy](T_Tessa_Web_Serialization_TypedJsonSerializerObjectPolicy.htm)|  
## __Перечисления
[TessaBsonCompressionMode](T_Tessa_Web_Serialization_TessaBsonCompressionMode.htm)|
Алгоритм сжатия содержимого, используемого при сериализации
[TessaBson](F_Tessa_Platform_Runtime_MediaTypes_TessaBson.htm).  
---|---  
[TypedJsonBodyFlags](T_Tessa_Web_Serialization_TypedJsonBodyFlags.htm)|
