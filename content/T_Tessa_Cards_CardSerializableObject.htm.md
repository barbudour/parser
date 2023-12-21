# CardSerializableObject - класс
Базовый объект для типа карточки или метаинформации, который может быть
сериализован в бинарную форму или в XML.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public abstract class CardSerializableObject : ValidationObject, 
    	IBinarySerializable, ISerializable, ISealable, IStorageSerializable
VB __Копировать
    <SerializableAttribute>
    Public MustInherit Class CardSerializableObject
    	Inherits ValidationObject
    	Implements IBinarySerializable, ISerializable, ISealable, IStorageSerializable
C++ __Копировать
    [SerializableAttribute]
    public ref class CardSerializableObject abstract : public ValidationObject, 
    	IBinarySerializable, ISerializable, ISealable, IStorageSerializable
F# __Копировать
     [<AbstractClassAttribute>]
    [<SerializableAttribute>]
    type CardSerializableObject = 
        class
            inherit ValidationObject
            interface IBinarySerializable
            interface ISerializable
            interface ISealable
            interface IStorageSerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm) __ CardSerializableObject
Derived
[Tessa.Cards.CardLibrary](T_Tessa_Cards_CardLibrary.htm)
[Tessa.Cards.CardLibraryItem](T_Tessa_Cards_CardLibraryItem.htm)
[Tessa.Cards.CardSchemeSerializableObject](T_Tessa_Cards_CardSchemeSerializableObject.htm)
[Tessa.Cards.CardTypeCompletionOption](T_Tessa_Cards_CardTypeCompletionOption.htm)
[Tessa.Cards.CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm)
[Tessa.Cards.CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
[Tessa.Cards.Metadata.CardMetadataRecord](T_Tessa_Cards_Metadata_CardMetadataRecord.htm)
[Tessa.Cards.Metadata.CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm)
Подробнее __Less __
Implements
    [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm), [ISealable](T_Tessa_Platform_ISealable.htm), [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)
##  __Конструкторы
[CardSerializableObject()](M_Tessa_Cards_CardSerializableObject__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[CardSerializableObject(SerializationInfo,
StreamingContext)](M_Tessa_Cards_CardSerializableObject__ctor_1.htm)|  Создаёт
экземпляр класса, десериализованный с использованием переданного объекта
[System.Runtime.Serialization.SerializationInfo].  
## __Свойства
[IsSealed](P_Tessa_Cards_CardSerializableObject_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
---|---  
[Reference](P_Tessa_Cards_CardSerializableObject_Reference.htm)|  Имя
глобального объекта, на который ссылается данный объект.  
[XmlElementNameInternal](P_Tessa_Cards_CardSerializableObject_XmlElementNameInternal.htm)|
Имя XML-элемента, для которого выполняется сериализация и десериализация.  
##  __Методы
[CheckSealed](M_Tessa_Cards_CardSerializableObject_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
---|---  
[CreateAndEnsureSealing<T>](M_Tessa_Cards_CardSerializableObject_CreateAndEnsureSealing__1.htm)|
Создаёт объект типа T посредством конструктора по умолчанию и защищает его от
изменений, если текущий объект также защищён от изменений.  
[CreateXmlWriter(Stream,
Boolean)](M_Tessa_Cards_CardSerializableObject_CreateXmlWriter.htm)|  Создаёт
объект
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter) для
сериализации объекта CardSerializableObject в XML, который записывается в
строковое представление в заданном объекте stream.  
[CreateXmlWriter(StringBuilder,
Boolean)](M_Tessa_Cards_CardSerializableObject_CreateXmlWriter_1.htm)|
Создаёт объект
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter) для
сериализации объекта CardSerializableObject в XML, который записывается в
строковое представление в заданном объекте stringBuilder.  
[DeserializeAttributeFromXml](M_Tessa_Cards_CardSerializableObject_DeserializeAttributeFromXml.htm)|
Выполняется для каждого атрибута десериализуемого атрибута.  
[DeserializeChildrenFromBinaryInternal](M_Tessa_Cards_CardSerializableObject_DeserializeChildrenFromBinaryInternal.htm)|
Выполняет десериализацию всех дочерних объектов из байтового потока.  
[DeserializeElementFromXml](M_Tessa_Cards_CardSerializableObject_DeserializeElementFromXml.htm)|
Выполняется для каждого элемента десериализуемого объекта.  
[DeserializeFromBinary(BinaryReader)](M_Tessa_Cards_CardSerializableObject_DeserializeFromBinary_1.htm)|
Выполняет десериализацию текущего объекта и всех его дочерних объектов из
байтового потока.  
[DeserializeFromBinary(Byte[])](M_Tessa_Cards_CardSerializableObject_DeserializeFromBinary.htm)|
Выполняет десериализацию текущего объекта и всех его дочерних объектов из
массива байт.  
[DeserializeFromBinary(Stream)](M_Tessa_Cards_CardSerializableObject_DeserializeFromBinary_2.htm)|
Выполняет десериализацию текущего объекта и всех его дочерних объектов из
байтового потока.  
[DeserializeFromBinaryInternal](M_Tessa_Cards_CardSerializableObject_DeserializeFromBinaryInternal.htm)|
Выполняет десериализацию всех полей текущего объекта из байтового потока.  
[DeserializeFromJson(String)](M_Tessa_Cards_CardSerializableObject_DeserializeFromJson.htm)|
Десериализует объект и его дочерние объекты из заданного текстового JSON с
сохраняемыми типами данных.  
[DeserializeFromJson<T>(String)](M_Tessa_Cards_CardSerializableObject_DeserializeFromJson__1.htm)|
Создаёт и объект и его дочерние объекты из заданного текстового JSON с
сохраняемыми типами данных.  
[DeserializeFromStorage(Dictionary<String,
Object>)](M_Tessa_Cards_CardSerializableObject_DeserializeFromStorage.htm)|
Десериализует объект и его дочерние объекты из заданного хранилища
Dictionary<string, object>.  
[DeserializeFromStorage<T>(Dictionary<String,
Object>)](M_Tessa_Cards_CardSerializableObject_DeserializeFromStorage__1.htm)|
Создаёт и десериализует объект из заданного хранилища Dictionary<string,
object>.  
[DeserializeFromStorageInternal](M_Tessa_Cards_CardSerializableObject_DeserializeFromStorageInternal.htm)|
Выполняет десериализацию объекта и всех его дочерних объектов из хранилища
Dictionary<string, object>.  
[DeserializeFromXml(Stream)](M_Tessa_Cards_CardSerializableObject_DeserializeFromXml.htm)|
Выполняет десериализацию объекта из XML из заданного потока.  
[DeserializeFromXml(String)](M_Tessa_Cards_CardSerializableObject_DeserializeFromXml_1.htm)|
Выполняет десериализацию объекта из XML, заданного посредством строки.  
[DeserializeFromXml(XmlReader)](M_Tessa_Cards_CardSerializableObject_DeserializeFromXml_2.htm)|
Выполняет десериализацию объекта и всех его дочерних объектов из элемента XML.  
[DeserializeGuidListFromBinary](M_Tessa_Cards_CardSerializableObject_DeserializeGuidListFromBinary.htm)|
Выполняет десериализацию заданного объекта SealableList<Guid> из байтового
потока посредством объекта
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader).  
[DeserializeGuidListFromStorage](M_Tessa_Cards_CardSerializableObject_DeserializeGuidListFromStorage.htm)|
Выполняет десериализацию заданного объекта SealableList<Guid> из хранилища
Dictionary<string, object>.  
[DeserializeGuidListFromXml](M_Tessa_Cards_CardSerializableObject_DeserializeGuidListFromXml.htm)|
Выполняет десериализацию заданного объекта SealableList<Guid> из XML-атрибута
с заданным значением.  
[DeserializeObjectFromBinary](M_Tessa_Cards_CardSerializableObject_DeserializeObjectFromBinary.htm)|
Десериализует объект из бинарного потока посредством объекта
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader).  
[DeserializeObjectFromStorage(Dictionary<String, Object>,
String)](M_Tessa_Cards_CardSerializableObject_DeserializeObjectFromStorage.htm)|
Десериализует объект из заданного хранилища Dictionary<string, object>.  
[DeserializeObjectFromStorage<T>(Dictionary<String, Object>,
String)](M_Tessa_Cards_CardSerializableObject_DeserializeObjectFromStorage__1.htm)|
Десериализует объект из заданного хранилища Dictionary<string, object>.  
[DeserializeObjectFromXml](M_Tessa_Cards_CardSerializableObject_DeserializeObjectFromXml.htm)|
Десериализует объект из XML-элемента в форме base64 посредством объекта
[XmlReader](https://learn.microsoft.com/dotnet/api/system.xml.xmlreader).  
[DeserializeObjectFromXmlToList<T>](M_Tessa_Cards_CardSerializableObject_DeserializeObjectFromXmlToList__1.htm)|
Выполняет десериализацию объекта CardSerializableObject из XML посредством
объекта
[XmlReader](https://learn.microsoft.com/dotnet/api/system.xml.xmlreader) и
добавление десериализованного объекта в заданную коллекцию.  
[DeserializeObjectListFromBinary<T>(BinaryReader,
SealableObjectList<T>)](M_Tessa_Cards_CardSerializableObject_DeserializeObjectListFromBinary__1.htm)|
Выполняет десериализацию коллекции объектов CardSerializableObject из
байтового потока посредством объекта
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader).  
[DeserializeObjectListFromBinary<TItem, TCollection>(BinaryReader,
TCollection, Func<Int32,
TCollection>)](M_Tessa_Cards_CardSerializableObject_DeserializeObjectListFromBinary__2.htm)|
Выполняет десериализацию коллекции объектов CardSerializableObject из
байтового потока посредством объекта
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader).  
[DeserializeObjectListFromStorage<T>(Dictionary<String, Object>, String,
Action<T>)](M_Tessa_Cards_CardSerializableObject_DeserializeObjectListFromStorage__1.htm)|
Выполняет десериализацию коллекции объектов CardSerializableObject из
хранилища Dictionary<string, object>.  
[DeserializeObjectListFromStorage<T>(Dictionary<String, Object>, String,
SealableObjectList<T>)](M_Tessa_Cards_CardSerializableObject_DeserializeObjectListFromStorage__1_1.htm)|
Выполняет десериализацию коллекции объектов CardSerializableObject из
хранилища Dictionary<string, object>.  
[DeserializeObjectListFromStorageWithMaterialization](M_Tessa_Cards_CardSerializableObject_DeserializeObjectListFromStorageWithMaterialization.htm)|
Выполняет десериализацию коллекции объектов CardSerializableObject из
хранилища Dictionary<string, object>.  
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
[GetObjectData](M_Tessa_Cards_CardSerializableObject_GetObjectData.htm)|
Записывает сериализованные данные текущего объекта в указанный объект
[System.Runtime.Serialization.SerializationInfo].  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetValidationName](M_Tessa_Platform_Validation_ValidationObject_GetValidationName.htm)|
Возвращает строку, определяющую имя объекта, или null, если имя объекта ещё
неизвестно или объект не содержит имени.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[IsValid](M_Tessa_Platform_Validation_ValidationObject_IsValid.htm)| Выполняет
проверку объекта на валидность и возвращает признак того, что объект является
валидным.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnDeserialized](M_Tessa_Cards_CardSerializableObject_OnDeserialized.htm)|
Выполняется после успешной десериализации объекта и всех его дочерних объектов
из элемента XML.  
[OnDeserializing](M_Tessa_Cards_CardSerializableObject_OnDeserializing.htm)|
Выполняется перед десериализацией объекта и всех его дочерних объектов из
элемента XML.  
[Seal](M_Tessa_Cards_CardSerializableObject_Seal.htm)| Защищает объект от
изменений.  
[SealInternal](M_Tessa_Cards_CardSerializableObject_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[SealNotNull](M_Tessa_Cards_CardSerializableObject_SealNotNull.htm)|  Защищает
от изменений заданный объект, если он не равен null.  
[SerializeAttributesToXml](M_Tessa_Cards_CardSerializableObject_SerializeAttributesToXml.htm)|
Выполняет сериализацию текущего объекта в атрибуты XML.  
[SerializeChildrenToBinaryInternal](M_Tessa_Cards_CardSerializableObject_SerializeChildrenToBinaryInternal.htm)|
Выполняет сериализацию всех дочерних объектов в байтовый поток.  
[SerializeElementsToXml](M_Tessa_Cards_CardSerializableObject_SerializeElementsToXml.htm)|
Выполняет сериализацию всех дочерних объектов для текущего объекта в элементы
XML.  
[SerializeGuidListToBinary](M_Tessa_Cards_CardSerializableObject_SerializeGuidListToBinary.htm)|
Выполняет сериализацию заданного объекта SealableList<Guid> в байтовый поток
посредством объекта
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter).  
[SerializeGuidListToStorage](M_Tessa_Cards_CardSerializableObject_SerializeGuidListToStorage.htm)|
Выполняет сериализацию заданного объекта SealableList<Guid> в хранилище
Dictionary<string, object>.  
[SerializeGuidListToXml](M_Tessa_Cards_CardSerializableObject_SerializeGuidListToXml.htm)|
Выполняет сериализацию заданного объекта SealableList<Guid> в XML-атрибут
посредством объекта
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter).  
[SerializeObjectListToBinary<T>](M_Tessa_Cards_CardSerializableObject_SerializeObjectListToBinary__1.htm)|
Выполняет сериализацию коллекции объектов CardSerializableObject в байтовый
поток посредством объекта
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter).  
[SerializeObjectListToStorage<T>(Dictionary<String, Object>, String,
ICollection<T>)](M_Tessa_Cards_CardSerializableObject_SerializeObjectListToStorage__1.htm)|
Выполняет сериализацию коллекции объектов CardSerializableObject в хранилище
Dictionary<string, object>.  
[SerializeObjectListToStorage<T>(Dictionary<String, Object>, String,
IEnumerable<KeyValuePair<String, T>>,
ICardSerializableContext)](M_Tessa_Cards_CardSerializableObject_SerializeObjectListToStorage__1_1.htm)|
Выполняет сериализацию хеш-таблицы объектов CardSerializableObject в хранилище
Dictionary<string, object>.  
[SerializeObjectListToStorage<T, TOrder>(Dictionary<String, Object>, String,
ICollection<T>, Func<T,
TOrder>)](M_Tessa_Cards_CardSerializableObject_SerializeObjectListToStorage__2.htm)|
Выполняет сериализацию коллекции объектов CardSerializableObject в хранилище
Dictionary<string, object>.  
[SerializeObjectListToXml<T>(XmlWriter,
ICollection<T>)](M_Tessa_Cards_CardSerializableObject_SerializeObjectListToXml__1.htm)|
Выполняет сериализацию коллекции объектов CardSerializableObject в XML
посредством объекта
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter).  
[SerializeObjectListToXml<T, TOrder>(XmlWriter, ICollection<T>, Func<T,
TOrder>)](M_Tessa_Cards_CardSerializableObject_SerializeObjectListToXml__2.htm)|
Выполняет сериализацию коллекции объектов CardSerializableObject в XML
посредством объекта
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter).  
[SerializeObjectToBinary](M_Tessa_Cards_CardSerializableObject_SerializeObjectToBinary.htm)|
Сериализует объект в бинарный поток посредством объекта
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter).  
[SerializeObjectToStorage(Dictionary<String, Object>, String,
CardSerializableObject)](M_Tessa_Cards_CardSerializableObject_SerializeObjectToStorage.htm)|
Сериализует объект в заданное хранилище Dictionary<string, object>.  
[SerializeObjectToStorage(Dictionary<String, Object>, String,
ISerializableObject)](M_Tessa_Cards_CardSerializableObject_SerializeObjectToStorage_1.htm)|
Сериализует объект в заданное хранилище Dictionary<string, object>.  
[SerializeObjectToXml](M_Tessa_Cards_CardSerializableObject_SerializeObjectToXml.htm)|
Сериализует объект в XML-элемент в форме base64 посредством объекта
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter), если
сериализуемый объект не равен null и непустой.  
[SerializeToBinary()](M_Tessa_Cards_CardSerializableObject_SerializeToBinary.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в массив
байт.  
[SerializeToBinary(BinaryWriter)](M_Tessa_Cards_CardSerializableObject_SerializeToBinary_1.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в
байтовый поток.  
[SerializeToBinary(Stream)](M_Tessa_Cards_CardSerializableObject_SerializeToBinary_2.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в
байтовый поток.  
[SerializeToBinaryInternal](M_Tessa_Cards_CardSerializableObject_SerializeToBinaryInternal.htm)|
Выполняет сериализацию текущего объекта в байтовый поток.  
[SerializeToJson](M_Tessa_Cards_CardSerializableObject_SerializeToJson.htm)|
Сериализует объект и его дочерние объекты в форме текстового JSON с
сохраняемыми типами данных.  
[SerializeToStorage()](M_Tessa_Cards_CardSerializableObject_SerializeToStorage.htm)|
Сериализует объект и его дочерние объекты в возвращаемое хранилище
Dictionary<string, object>.  
[SerializeToStorage(Dictionary<String,
Object>)](M_Tessa_Cards_CardSerializableObject_SerializeToStorage_1.htm)|
Сериализует объект и его дочерние объекты в заданное хранилище
Dictionary<string, object>.  
[SerializeToStorageInternal](M_Tessa_Cards_CardSerializableObject_SerializeToStorageInternal.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в
хранилище Dictionary<string, object>.  
[SerializeToXml(Boolean)](M_Tessa_Cards_CardSerializableObject_SerializeToXml.htm)|
Возвращает строку, которая содержит сериализованный в XML объект.  
[SerializeToXml(XmlWriter)](M_Tessa_Cards_CardSerializableObject_SerializeToXml_2.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в элемент
XML.  
[SerializeToXml(Stream,
Boolean)](M_Tessa_Cards_CardSerializableObject_SerializeToXml_1.htm)|
Выполняет сериализацию объекта в XML в заданный поток.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Validate()](M_Tessa_Platform_Validation_ValidationObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[ValidateInternal](M_Tessa_Platform_Validation_ValidationObject_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
##  __Поля
[BinaryDataSerializationKey](F_Tessa_Cards_CardSerializableObject_BinaryDataSerializationKey.htm)|
Ключ, описывающий сериализованное состояние объекта в виде байтового массива,
которое задаётся или получается посредством объекта
[System.Runtime.Serialization.SerializationInfo].  
---|---  
[ReferenceKey](F_Tessa_Cards_CardSerializableObject_ReferenceKey.htm)|  
[TypeKey](F_Tessa_Cards_CardSerializableObject_TypeKey.htm)|  
## __Методы расширения
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
[ToSerializedDictionary](M_Tessa_Platform_Storage_StorageExtensions_ToSerializedDictionary.htm)|
Сериализует объект в нетипизированный словарь.  
(Определяется
[StorageExtensions](T_Tessa_Platform_Storage_StorageExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
