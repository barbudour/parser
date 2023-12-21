# SessionSerializableObject - класс
Сериализуемый объект, используемый в сессии Tessa.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public abstract class SessionSerializableObject : ISessionSerializableObject, 
    	IBinarySerializable, IBsonSerializable, IJsonSerializable, ISealable, ISerializable
VB __Копировать
    <SerializableAttribute>
    Public MustInherit Class SessionSerializableObject
    	Implements ISessionSerializableObject, IBinarySerializable, IBsonSerializable, IJsonSerializable, 
    	ISealable, ISerializable
C++ __Копировать
    [SerializableAttribute]
    public ref class SessionSerializableObject abstract : ISessionSerializableObject, 
    	IBinarySerializable, IBsonSerializable, IJsonSerializable, ISealable, ISerializable
F# __Копировать
     [<AbstractClassAttribute>]
    [<SerializableAttribute>]
    type SessionSerializableObject = 
        class
            interface ISessionSerializableObject
            interface IBinarySerializable
            interface IBsonSerializable
            interface IJsonSerializable
            interface ISealable
            interface ISerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SessionSerializableObject
Derived
[Tessa.Platform.Runtime.SessionToken](T_Tessa_Platform_Runtime_SessionToken.htm)
Implements
    [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm), [IBsonSerializable](T_Tessa_Platform_IBsonSerializable.htm), [IJsonSerializable](T_Tessa_Platform_IJsonSerializable.htm), [ISealable](T_Tessa_Platform_ISealable.htm), [ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm)
##  __Конструкторы
[SessionSerializableObject()](M_Tessa_Platform_Runtime_SessionSerializableObject__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[SessionSerializableObject(SerializationInfo,
StreamingContext)](M_Tessa_Platform_Runtime_SessionSerializableObject__ctor_1.htm)|
Создаёт экземпляр класса, десериализованный с использованием переданного
объекта [System.Runtime.Serialization.SerializationInfo].  
## __Свойства
[IsSealed](P_Tessa_Platform_Runtime_SessionSerializableObject_IsSealed.htm)|
Признак того, что объект был защищён от изменений.  
---|---  
[XmlElementName](P_Tessa_Platform_Runtime_SessionSerializableObject_XmlElementName.htm)|
Имя элемента XML для сериализуемого объекта сессии.  
##  __Методы
[CheckSealed](M_Tessa_Platform_Runtime_SessionSerializableObject_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
---|---  
[CreateXmlWriter(Stream)](M_Tessa_Platform_Runtime_SessionSerializableObject_CreateXmlWriter.htm)|
Создаёт объект
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter) для
сериализации объекта SessionSerializableObject в XML, который записывается в
строковое представление в заданном объекте stream.  
[CreateXmlWriter(StringBuilder)](M_Tessa_Platform_Runtime_SessionSerializableObject_CreateXmlWriter_1.htm)|
Создаёт объект
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter) для
сериализации объекта SessionSerializableObject в XML, который записывается в
строковое представление в заданном объекте stringBuilder.  
[DeserializeAttributeFromXmlCore](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeAttributeFromXmlCore.htm)|
Выполняется для каждого атрибута десериализуемого атрибута.  
[DeserializeElementFromXmlCore](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeElementFromXmlCore.htm)|
Выполняется для каждого элемента десериализуемого объекта.  
[DeserializeFromBase64Core](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromBase64Core.htm)|
Выполняет десериализацию объекта, сериализованного в виде base64-строки в
указанном массиве байт.  
[DeserializeFromBinaryCore(BinaryReader)](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromBinaryCore_1.htm)|
Выполняет десериализацию объекта, сериализованного в бинарном виде, используя
указанный объект для чтения.  
[DeserializeFromBinaryCore(Byte[])](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromBinaryCore.htm)|
Выполняет десериализацию объекта, сериализованного в бинарном виде в указанном
массиве байт.  
[DeserializeFromStorageCore](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromStorageCore.htm)|
Выполняет десериализацию объекта из заданного сериализуемого хранилища
Dictionary<string, object>.  
[DeserializeFromXmlCore(Stream)](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromXmlCore.htm)|
Выполняет десериализацию объекта из XML из заданного потока.  
[DeserializeFromXmlCore(String)](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromXmlCore_1.htm)|
Выполняет десериализацию объекта из XML, заданного посредством строки.  
[DeserializeFromXmlCore(XmlReader)](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromXmlCore_2.htm)|
Выполняет десериализацию объекта и всех его дочерних объектов из элемента XML.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateSerializationCache](M_Tessa_Platform_Runtime_SessionSerializableObject_InvalidateSerializationCache.htm)|
Сбрасывает кэш сериализованных данных, которые ускоряют повторную
сериализацию. Требуется вызывать этот метод после любого изменения свойств.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnDeserializing](M_Tessa_Platform_Runtime_SessionSerializableObject_OnDeserializing.htm)|
Выполняется перед десериализацией объекта. В методе рекомендуется заполнить
значения полей по умолчанию.  
[Seal](M_Tessa_Platform_Runtime_SessionSerializableObject_Seal.htm)| Защищает
объект от изменений.  
[SealInternal](M_Tessa_Platform_Runtime_SessionSerializableObject_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[SerializeAttributesToXmlCore](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeAttributesToXmlCore.htm)|
Выполняет сериализацию текущего объекта в атрибуты XML.  
[SerializeElementsToXmlCore](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeElementsToXmlCore.htm)|
Выполняет сериализацию всех дочерних объектов для текущего объекта в элементы
XML.  
[SerializeToBase64](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToBase64.htm)|
Выполняет сериализацию объекта в виде base64-строки.  
[SerializeToBinary(SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToBinary_1.htm)|
Выполняет сериализацию объекта в виде массива байт.  
[SerializeToBinary(BinaryWriter,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToBinary.htm)|
Выполняет сериализацию объекта в бинарном виде, используя указанный объект для
записи.  
[SerializeToBinaryCore](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToBinaryCore.htm)|
Выполняет сериализацию объекта в бинарном виде, используя указанный объект для
записи.  
[SerializeToStorage(SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToStorage_1.htm)|
Выполняет сериализацию объекта в сериализуемое хранилище Dictionary<string,
object>. Может использоваться для сериализации в Bson.  
[SerializeToStorage(Dictionary<String, Object>,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToStorage.htm)|
Выполняет сериализацию объекта в заданное сериализуемое хранилище
Dictionary<string, object>. Может использоваться для сериализации в Bson.  
[SerializeToStorageCore](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToStorageCore.htm)|
Выполняет сериализацию объекта в заданное сериализуемое хранилище
Dictionary<string, object>. Может использоваться для сериализации в Bson.  
[SerializeToXml(SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToXml_2.htm)|
Возвращает строку, которая содержит сериализованный в XML объект.  
[SerializeToXml(Stream,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToXml.htm)|
Выполняет сериализацию объекта в XML в заданный поток.  
[SerializeToXml(XmlWriter,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToXml_1.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в элемент
XML.  
[ToString](M_Tessa_Platform_Runtime_SessionSerializableObject_ToString.htm)|
Возвращает строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
