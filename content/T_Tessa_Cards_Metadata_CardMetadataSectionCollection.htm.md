# CardMetadataSectionCollection - класс
Коллекция, содержащая объекты
[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class CardMetadataSectionCollection : CardSerializableEntryCollection<CardMetadataSection>
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class CardMetadataSectionCollection
    	Inherits CardSerializableEntryCollection(Of CardMetadataSection)
C++ __Копировать
    [SerializableAttribute]
    public ref class CardMetadataSectionCollection sealed : public CardSerializableEntryCollection<CardMetadataSection^>
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type CardMetadataSectionCollection = 
        class
            inherit CardSerializableEntryCollection<CardMetadataSection>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm) __[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) __[CardSchemeSerializableObject](T_Tessa_Cards_CardSchemeSerializableObject.htm) __[CardSerializableEntryCollection](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)<[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)> __ CardMetadataSectionCollection
##  __Конструкторы
[CardMetadataSectionCollection()](M_Tessa_Cards_Metadata_CardMetadataSectionCollection__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[CardMetadataSectionCollection(IEnumerable<CardMetadataSection>)](M_Tessa_Cards_Metadata_CardMetadataSectionCollection__ctor_1.htm)|
Создаёт экземпляр класса с указанием коллекции элементов.  
[CardMetadataSectionCollection(Int32)](M_Tessa_Cards_Metadata_CardMetadataSectionCollection__ctor_2.htm)|
Создаёт экземпляр класса с указанием начальной вместимости списка.  
##  __Свойства
[Count](P_Tessa_Cards_CardSerializableEntryCollection_1_Count.htm)| Количество
элементов в коллекции.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
---|---  
[IsReadOnly](P_Tessa_Cards_CardSerializableEntryCollection_1_IsReadOnly.htm)|
Признак доступности коллекции только для чтения.
Свойство возвращает значение свойства [Tessa.Platform.ISealable.IsSealed].
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[IsSealed](P_Tessa_Cards_CardSerializableObject_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[Item[Guid]](P_Tessa_Cards_CardSerializableEntryCollection_1_Item.htm)|
Возвращает элемент коллекции по его идентификатору.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[Item[Int32]](P_Tessa_Cards_CardSerializableEntryCollection_1_Item_1.htm)|
Возвращает элемент коллекции по его индексу в списке.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[Item[String]](P_Tessa_Cards_CardSerializableEntryCollection_1_Item_2.htm)|
Возвращает элемент коллекции по его имени.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[Reference](P_Tessa_Cards_CardSerializableObject_Reference.htm)|  Имя
глобального объекта, на который ссылается данный объект.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[XmlElementNameInternal](P_Tessa_Cards_Metadata_CardMetadataSectionCollection_XmlElementNameInternal.htm)|
Имя XML-элемента, для которого выполняется сериализация и десериализация.  
(Переопределяет
[CardSerializableObject.XmlElementNameInternal](P_Tessa_Cards_CardSerializableObject_XmlElementNameInternal.htm))  
[XmlItemNameInternal](P_Tessa_Cards_Metadata_CardMetadataSectionCollection_XmlItemNameInternal.htm)|
Имя входящих в коллекцию XML-элементов, для которых выполняется сериализация и
десериализация.  
(Переопределяет
[CardSerializableEntryCollection<T>.XmlItemNameInternal](P_Tessa_Cards_CardSerializableEntryCollection_1_XmlItemNameInternal.htm))  
##  __Методы
[Add](M_Tessa_Cards_CardSerializableEntryCollection_1_Add.htm)| Добавляет
заданный элемент в коллекцию.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
---|---  
[CheckSealed](M_Tessa_Cards_CardSerializableObject_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[Clear](M_Tessa_Cards_CardSerializableEntryCollection_1_Clear.htm)| Удаляет
все элементы коллекции.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[Contains(T)](M_Tessa_Cards_CardSerializableEntryCollection_1_Contains_2.htm)|
Возвращает признак того, что заданный элемент содержится в коллекции.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[Contains(Guid)](M_Tessa_Cards_CardSerializableEntryCollection_1_Contains.htm)|
Возвращает признак того, что элемент с заданным идентификатором присутствует в
коллекции.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[Contains(String)](M_Tessa_Cards_CardSerializableEntryCollection_1_Contains_1.htm)|
Возвращает признак того, что элемент с заданным именем присутствует в
коллекции.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[CopyTo](M_Tessa_Cards_CardSerializableEntryCollection_1_CopyTo.htm)| Копирует
элементы коллекции в массив, начиная с заданного отсчитываемого от нуля
индекса.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[CreateAndEnsureSealing<T>](M_Tessa_Cards_CardSerializableObject_CreateAndEnsureSealing__1.htm)|
Создаёт объект типа T посредством конструктора по умолчанию и защищает его от
изменений, если текущий объект также защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DeserializeAttributeFromXml](M_Tessa_Cards_CardSerializableObject_DeserializeAttributeFromXml.htm)|
Выполняется для каждого атрибута десериализуемого атрибута.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DeserializeChildrenFromBinaryInternal](M_Tessa_Cards_CardSerializableEntryCollection_1_DeserializeChildrenFromBinaryInternal.htm)|
Выполняет десериализацию всех дочерних объектов из байтового потока.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[DeserializeElementFromXml](M_Tessa_Cards_CardSerializableEntryCollection_1_DeserializeElementFromXml.htm)|
Выполняется для каждого элемента десериализуемого объекта.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[DeserializeFromBinary(BinaryReader)](M_Tessa_Cards_CardSerializableObject_DeserializeFromBinary_1.htm)|
Выполняет десериализацию текущего объекта и всех его дочерних объектов из
байтового потока.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DeserializeFromBinary(Byte[])](M_Tessa_Cards_CardSerializableObject_DeserializeFromBinary.htm)|
Выполняет десериализацию текущего объекта и всех его дочерних объектов из
массива байт.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DeserializeFromBinary(Stream)](M_Tessa_Cards_CardSerializableObject_DeserializeFromBinary_2.htm)|
Выполняет десериализацию текущего объекта и всех его дочерних объектов из
байтового потока.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DeserializeFromBinaryInternal](M_Tessa_Cards_CardSerializableObject_DeserializeFromBinaryInternal.htm)|
Выполняет десериализацию всех полей текущего объекта из байтового потока.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DeserializeFromJson(String)](M_Tessa_Cards_CardSerializableObject_DeserializeFromJson.htm)|
Десериализует объект и его дочерние объекты из заданного текстового JSON с
сохраняемыми типами данных.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DeserializeFromStorage(Dictionary<String,
Object>)](M_Tessa_Cards_CardSerializableObject_DeserializeFromStorage.htm)|
Десериализует объект и его дочерние объекты из заданного хранилища
Dictionary<string, object>.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DeserializeFromStorage(Dictionary<String, Object>,
String)](M_Tessa_Cards_CardSerializableEntryCollection_1_DeserializeFromStorage.htm)|
Десериализует объект и его дочерние объекты из заданного хранилища
Dictionary<string, object>.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[DeserializeFromStorageInternal](M_Tessa_Cards_CardSerializableObject_DeserializeFromStorageInternal.htm)|
Выполняет десериализацию объекта и всех его дочерних объектов из хранилища
Dictionary<string, object>.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DeserializeFromXml(Stream)](M_Tessa_Cards_CardSerializableObject_DeserializeFromXml.htm)|
Выполняет десериализацию объекта из XML из заданного потока.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DeserializeFromXml(String)](M_Tessa_Cards_CardSerializableObject_DeserializeFromXml_1.htm)|
Выполняет десериализацию объекта из XML, заданного посредством строки.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DeserializeFromXml(XmlReader)](M_Tessa_Cards_CardSerializableObject_DeserializeFromXml_2.htm)|
Выполняет десериализацию объекта и всех его дочерних объектов из элемента XML.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
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
[GetChildRowSections(Guid)](M_Tessa_Cards_Metadata_CardMetadataSectionCollection_GetChildRowSections.htm)|
Возвращает дочерние коллекционные или древовидные секции для секции с заданным
идентификатором.  
[GetChildRowSections(String)](M_Tessa_Cards_Metadata_CardMetadataSectionCollection_GetChildRowSections_1.htm)|
Возвращает дочерние коллекционные или древовидные секции для секции с заданным
именем.  
[GetEnumerator](M_Tessa_Cards_CardSerializableEntryCollection_1_GetEnumerator.htm)|
Возвращает итератор по элементам коллекции.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetObjectData](M_Tessa_Cards_CardSerializableObject_GetObjectData.htm)|
Записывает сериализованные данные текущего объекта в указанный объект
[System.Runtime.Serialization.SerializationInfo].  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
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
[IndexOf](M_Tessa_Cards_CardSerializableEntryCollection_1_IndexOf.htm)|
Возвращает отсчитываемый от нуля индекс заданного элемента в коллекции.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[Insert](M_Tessa_Cards_CardSerializableEntryCollection_1_Insert.htm)|
Вставляет элемент в заданную позицию.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
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
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[OnDeserializing](M_Tessa_Cards_CardSerializableEntryCollection_1_OnDeserializing.htm)|
Выполняется перед десериализацией объекта и всех его дочерних объектов из
элемента XML.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[OnItemAttributeSerializationToXml](M_Tessa_Cards_CardSerializableEntryCollection_1_OnItemAttributeSerializationToXml.htm)|
Происходит перед сериализацией элементов коллекции в XML-элемент.
При переопределении метода в него можно добавить логику по дополнению XML-
элемента атрибутами, которые не были добавлены методом сериализации самого
элемента коллекции, но которые обрабатываются при десериализации XML-элемента.
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[Remove(T)](M_Tessa_Cards_CardSerializableEntryCollection_1_Remove_2.htm)|
Удаляет заданный элемент из коллекции.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[Remove(Guid)](M_Tessa_Cards_CardSerializableEntryCollection_1_Remove.htm)|
Удаляет элемент с заданным идентификатором из коллекции.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[Remove(String)](M_Tessa_Cards_CardSerializableEntryCollection_1_Remove_1.htm)|
Удаляет элемент с заданным именем из коллекции.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[RemoveAt](M_Tessa_Cards_CardSerializableEntryCollection_1_RemoveAt.htm)|
Удаляет элемент в заданной позиции.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[RepairAsync(ICardSchemeInfoProvider,
CancellationToken)](M_Tessa_Cards_CardSchemeSerializableObject_RepairAsync.htm)|
Метод восстанавливает объект к работоспособному состоянии в соответствии со
схемой. Этот процесс включает удаление данных из текущего объекта, которые
имеют отношение к схеме, но фактически в ней отсутствуют.  
(Унаследован от
[CardSchemeSerializableObject](T_Tessa_Cards_CardSchemeSerializableObject.htm))  
[RepairAsync(ICardSchemeInfoProvider, IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_CardSchemeSerializableObject_RepairAsync_1.htm)|
Метод восстанавливает объект к работоспособному состоянии в соответствии со
схемой. Этот процесс включает удаление данных из текущего объекта, которые
имеют отношение к схеме, но фактически в ней отсутствуют.  
(Унаследован от
[CardSchemeSerializableObject](T_Tessa_Cards_CardSchemeSerializableObject.htm))  
[RepairInternalAsync](M_Tessa_Cards_CardSerializableEntryCollection_1_RepairInternalAsync.htm)|
Метод восстанавливает объект к работоспособному состоянии в соответствии со
схемой. Этот процесс включает удаление данных из текущего объекта, которые
имеют отношение к схеме, но фактически в ней отсутствуют.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[Seal](M_Tessa_Cards_CardSerializableObject_Seal.htm)| Защищает объект от
изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SealInternal](M_Tessa_Cards_CardSerializableEntryCollection_1_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[SerializeAttributesToXml](M_Tessa_Cards_CardSerializableObject_SerializeAttributesToXml.htm)|
Выполняет сериализацию текущего объекта в атрибуты XML.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SerializeChildrenToBinaryInternal](M_Tessa_Cards_CardSerializableEntryCollection_1_SerializeChildrenToBinaryInternal.htm)|
Выполняет сериализацию всех дочерних объектов в байтовый поток.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[SerializeElementsToXml](M_Tessa_Cards_CardSerializableEntryCollection_1_SerializeElementsToXml.htm)|
Выполняет сериализацию всех дочерних объектов для текущего объекта в элементы
XML.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[SerializeToBinary()](M_Tessa_Cards_CardSerializableObject_SerializeToBinary.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в массив
байт.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SerializeToBinary(BinaryWriter)](M_Tessa_Cards_CardSerializableObject_SerializeToBinary_1.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в
байтовый поток.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SerializeToBinary(Stream)](M_Tessa_Cards_CardSerializableObject_SerializeToBinary_2.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в
байтовый поток.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SerializeToBinaryInternal](M_Tessa_Cards_CardSerializableObject_SerializeToBinaryInternal.htm)|
Выполняет сериализацию текущего объекта в байтовый поток.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SerializeToJson](M_Tessa_Cards_CardSerializableObject_SerializeToJson.htm)|
Сериализует объект и его дочерние объекты в форме текстового JSON с
сохраняемыми типами данных.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SerializeToStorage()](M_Tessa_Cards_CardSerializableObject_SerializeToStorage.htm)|
Сериализует объект и его дочерние объекты в возвращаемое хранилище
Dictionary<string, object>.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SerializeToStorage(Dictionary<String,
Object>)](M_Tessa_Cards_CardSerializableObject_SerializeToStorage_1.htm)|
Сериализует объект и его дочерние объекты в заданное хранилище
Dictionary<string, object>.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SerializeToStorage(Dictionary<String, Object>,
String)](M_Tessa_Cards_CardSerializableEntryCollection_1_SerializeToStorage.htm)|
Сериализует объект и его дочерние объекты в заданное хранилище
Dictionary<string, object>.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[SerializeToStorageInternal](M_Tessa_Cards_CardSerializableObject_SerializeToStorageInternal.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в
хранилище Dictionary<string, object>.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SerializeToXml(Boolean)](M_Tessa_Cards_CardSerializableObject_SerializeToXml.htm)|
Возвращает строку, которая содержит сериализованный в XML объект.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SerializeToXml(XmlWriter)](M_Tessa_Cards_CardSerializableObject_SerializeToXml_2.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в элемент
XML.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SerializeToXml(Stream,
Boolean)](M_Tessa_Cards_CardSerializableObject_SerializeToXml_1.htm)|
Выполняет сериализацию объекта в XML в заданный поток.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetValue(Guid,
T)](M_Tessa_Cards_CardSerializableEntryCollection_1_TryGetValue.htm)|
Пытается вернуть элемент коллекции по его идентификатору.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[TryGetValue(String,
T)](M_Tessa_Cards_CardSerializableEntryCollection_1_TryGetValue_1.htm)|
Пытается вернуть элемент коллекции по его имени.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
[Validate()](M_Tessa_Platform_Validation_ValidationObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[ValidateInternal](M_Tessa_Cards_CardSerializableEntryCollection_1_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm))  
##  __Поля
[XmlElementName](F_Tessa_Cards_Metadata_CardMetadataSectionCollection_XmlElementName.htm)|
Имя XML-элемента.  
---|---  
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
[TryGetIgnoreCase](M_Tessa_Cards_CardExtensions_TryGetIgnoreCase_1.htm)|
Возвращает секцию из метаинформации, полученную без учёта регистра, или null,
если такая секция отсутствует.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
