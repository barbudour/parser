# Tessa.Platform.Json - пространство имён
API сериализации в текстовый JSON или бинарный BSON.
##  __Классы
[GuidConverter](T_Tessa_Platform_Json_GuidConverter.htm)|  Конвертер
используемый только для записи Guid при сериализации c помощью JsonSerializer.
Преобразует Guid из xxxx-xxxxxx-xxxxx-xxxx в xxxxxxxxxxxxxxxxxxxx. Для
обратной конвертации используется следует исползовать стандартный конвертер.  
---|---  
[SchemeTypeConverter](T_Tessa_Platform_Json_SchemeTypeConverter.htm)|  The
tessa type converter.  
[TessaBsonSerializer](T_Tessa_Platform_Json_TessaBsonSerializer.htm)|  The
tessa serializer.  
[TessaJsonConverter](T_Tessa_Platform_Json_TessaJsonConverter.htm)|  Конвертер
JSON, выполняющий сериализацию объектов с поддержкой интерфейсов
[IJsonSerializable](T_Tessa_Platform_IJsonSerializable.htm) и
[IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm). Для бинарной
сериализации выполняется преобразование в объект, в котором по ключу
[Base64Key](F_Tessa_Platform_Json_TessaJsonConverter_Base64Key.htm) содержится
бинарное представление в виде base64-строки. Конвертер используется, например,
для обмена данными с веб-сервисами ASP.NET Core. Чтобы задействовать
сериализатор по умолчанию с этим конвертером рекомендуется использовать
свойство [Json](P_Tessa_Platform_Json_TessaSerializer_Json.htm).  
[TessaJsonSerializationContext](T_Tessa_Platform_Json_TessaJsonSerializationContext.htm)|
Контекст операции для сериализации/десериализации с учетом
[JsonTextPart](T_Tessa_Platform_Json_JsonTextPart.htm)  
[TessaSerializationException](T_Tessa_Platform_Json_TessaSerializationException.htm)|
Исключение при сериализации или десериализации объектов посредством
[TessaSerializer](T_Tessa_Platform_Json_TessaSerializer.htm).  
[TessaSerializer](T_Tessa_Platform_Json_TessaSerializer.htm)|  
[TypedJsonConverter](T_Tessa_Platform_Json_TypedJsonConverter.htm)|  
[UnknownTessaJsonSerializationContextException](T_Tessa_Platform_Json_UnknownTessaJsonSerializationContextException.htm)|
Исключение, возникающее при отсутствии контекста
[ITessaJsonSerializationContext](T_Tessa_Platform_Json_ITessaJsonSerializationContext.htm)
при сериализации/десериализации JSON с объектами
[JsonTextPart](T_Tessa_Platform_Json_JsonTextPart.htm)  
##  __Структуры
[JsonTextPart](T_Tessa_Platform_Json_JsonTextPart.htm)|
Контейнер для сериализации/десериализации в JSON, позволяющий разбить
multiline строку на 2 части \-
[Alias](P_Tessa_Platform_Json_JsonTextPart_Alias.htm), который запишется в
значение по ключу, и Content, который должен быть дописан после конца JSON
(после закрывающей скобки).
Для корректного использования при сериализации/десериализации с помощью
[TypedJsonConverter](T_Tessa_Platform_Json_TypedJsonConverter.htm) нужно
создать область операции для контекста
[ITessaJsonSerializationContext](T_Tessa_Platform_Json_ITessaJsonSerializationContext.htm),
в который будут помещены все найденные
[JsonTextPart](T_Tessa_Platform_Json_JsonTextPart.htm).
Запись происходит в формате:  
[TEXTPART Alias]  
Content  
---|---  
##  __Интерфейсы
[ITessaJsonSerializationContext](T_Tessa_Platform_Json_ITessaJsonSerializationContext.htm)|  
---|---
