# ISessionSerializableObject - интерфейс
Сериализуемый объект, используемый в сессии Tessa.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISessionSerializableObject : IBinarySerializable, 
    	IBsonSerializable, IJsonSerializable
VB __Копировать
     Public Interface ISessionSerializableObject
    	Inherits IBinarySerializable, IBsonSerializable, IJsonSerializable
C++ __Копировать
     public interface class ISessionSerializableObject : IBinarySerializable, 
    	IBsonSerializable, IJsonSerializable
F# __Копировать
     type ISessionSerializableObject = 
        interface
            interface IBinarySerializable
            interface IBsonSerializable
            interface IJsonSerializable
        end
Implements
    [IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm), [IBsonSerializable](T_Tessa_Platform_IBsonSerializable.htm), [IJsonSerializable](T_Tessa_Platform_IJsonSerializable.htm)
##  __Методы
[Deserialize(BinaryReader)](M_Tessa_Platform_IBinarySerializable_Deserialize.htm)|
Десериализует объект из бинарной формы.  
(Унаследован от
[IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm))  
---|---  
[Deserialize(BsonReader)](M_Tessa_Platform_IBsonSerializable_Deserialize.htm)|
Выполняет десериализацию объекта из бинарного JSON.  
(Унаследован от [IBsonSerializable](T_Tessa_Platform_IBsonSerializable.htm))  
[Deserialize(JsonReader)](M_Tessa_Platform_IJsonSerializable_Deserialize.htm)|
Выполняет десериализацию объекта из JSON.  
(Унаследован от [IJsonSerializable](T_Tessa_Platform_IJsonSerializable.htm))  
[Serialize(BinaryWriter)](M_Tessa_Platform_IBinarySerializable_Serialize.htm)|
Сериализует объект в бинарной форме.  
(Унаследован от
[IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm))  
[Serialize(BsonWriter)](M_Tessa_Platform_IBsonSerializable_Serialize.htm)|
Выполняет сериализацию объекта в бинарный JSON. Возвращает строку текста,
содержащую сериализованный объект.  
(Унаследован от [IBsonSerializable](T_Tessa_Platform_IBsonSerializable.htm))  
[Serialize(JsonWriter)](M_Tessa_Platform_IJsonSerializable_Serialize.htm)|
Выполняет сериализацию объекта в JSON. Возвращает строку текста, содержащую
сериализованный объект.  
(Унаследован от [IJsonSerializable](T_Tessa_Platform_IJsonSerializable.htm))  
[SerializeToBase64](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToBase64.htm)|
Выполняет сериализацию объекта в виде base64-строки.  
[SerializeToBinary(SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToBinary_1.htm)|
Выполняет сериализацию объекта в виде массива байт.  
[SerializeToBinary(BinaryWriter,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToBinary.htm)|
Выполняет сериализацию объекта в бинарном виде, используя указанный объект для
записи.  
[SerializeToStorage(SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToStorage_1.htm)|
Выполняет сериализацию объекта в сериализуемое хранилище Dictionary<string,
object>. Может использоваться для сериализации в Bson.  
[SerializeToStorage(Dictionary<String, Object>,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToStorage.htm)|
Выполняет сериализацию объекта в заданное сериализуемое хранилище
Dictionary<string, object>. Может использоваться для сериализации в Bson.  
[SerializeToXml(SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToXml_2.htm)|
Возвращает строку, которая содержит сериализованный в XML объект.  
[SerializeToXml(Stream,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToXml.htm)|
Выполняет сериализацию объекта в XML в заданный поток.  
[SerializeToXml(XmlWriter,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToXml_1.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в элемент
XML.  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
