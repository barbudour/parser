# CardSerializableEntryCollection<T> \- класс
Коллекция, содержащая сериализуемые в бинарную форму и в XML объекты, для
которых определён способ доступа по имени и по идентификатору.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public abstract class CardSerializableEntryCollection<T> : CardSchemeSerializableObject, 
    	IList<T>, ICollection<T>, IEnumerable<T>, IEnumerable, IList, 
    	ICollection, IReadOnlyList<T>, IReadOnlyCollection<T>
    where T : new(), CardSerializableObject, ICardSerializableEntry
VB __Копировать
    <SerializableAttribute>
    Public MustInherit Class CardSerializableEntryCollection(Of T As {New, CardSerializableObject, ICardSerializableEntry})
    	Inherits CardSchemeSerializableObject
    	Implements IList(Of T), ICollection(Of T), 
    	IEnumerable(Of T), IEnumerable, IList, ICollection, IReadOnlyList(Of T), 
    	IReadOnlyCollection(Of T)
C++ __Копировать
    [SerializableAttribute]
    generic<typename T>
    where T : gcnew(), CardSerializableObject, ICardSerializableEntry
    public ref class CardSerializableEntryCollection abstract : public CardSchemeSerializableObject, 
    	IList<T>, ICollection<T>, IEnumerable<T>, IEnumerable, IList, 
    	ICollection, IReadOnlyList<T>, IReadOnlyCollection<T>
F# __Копировать
     [<AbstractClassAttribute>]
    [<SerializableAttribute>]
    type CardSerializableEntryCollection<'T when 'T : new() and CardSerializableObject and ICardSerializableEntry> = 
        class
            inherit CardSchemeSerializableObject
            interface IList<'T>
            interface ICollection<'T>
            interface IEnumerable<'T>
            interface IEnumerable
            interface IList
            interface ICollection
            interface IReadOnlyList<'T>
            interface IReadOnlyCollection<'T>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm) __[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) __[CardSchemeSerializableObject](T_Tessa_Cards_CardSchemeSerializableObject.htm) __ CardSerializableEntryCollection<T>
Derived
[Tessa.Cards.CardTypeCollection](T_Tessa_Cards_CardTypeCollection.htm)
[Tessa.Cards.Metadata.CardMetadataColumnCollection](T_Tessa_Cards_Metadata_CardMetadataColumnCollection.htm)
[Tessa.Cards.Metadata.CardMetadataCompletionOptionCollection](T_Tessa_Cards_Metadata_CardMetadataCompletionOptionCollection.htm)
[Tessa.Cards.Metadata.CardMetadataEnumerationCollection](T_Tessa_Cards_Metadata_CardMetadataEnumerationCollection.htm)
[Tessa.Cards.Metadata.CardMetadataEnumerationColumnCollection](T_Tessa_Cards_Metadata_CardMetadataEnumerationColumnCollection.htm)
[Tessa.Cards.Metadata.CardMetadataFunctionRoleCollection](T_Tessa_Cards_Metadata_CardMetadataFunctionRoleCollection.htm)
[Tessa.Cards.Metadata.CardMetadataSectionCollection](T_Tessa_Cards_Metadata_CardMetadataSectionCollection.htm)
[Tessa.Cards.VirtualScheme.CardTypeColumnCollection](T_Tessa_Cards_VirtualScheme_CardTypeColumnCollection.htm)
Подробнее __Less __
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<T>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<T>, [IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<T>, [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<T>, [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<T>, [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.icollection), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist)
#### Параметры типа
T
Ссылочный тип элементов коллекции, унаследованный от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm),
дополнительно реализующий интерфейс
[ICardSerializableEntry](T_Tessa_Cards_ICardSerializableEntry.htm) и
содержащий конструктор по умолчанию.
Для такого объекта также должен быть переопределён метод сравнения
[Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)) таким образом, чтобы он сравнивал объекты по
равенству идентификаторов.
##  __Заметки
В качестве элементов коллекции удобно использовать наследников класса
[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm).
## __Конструкторы
[CardSerializableEntryCollection<T>()](M_Tessa_Cards_CardSerializableEntryCollection_1__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[CardSerializableEntryCollection<T>(IEnumerable<T>)](M_Tessa_Cards_CardSerializableEntryCollection_1__ctor_1.htm)|
Создаёт экземпляр класса с указанием коллекции элементов.  
[CardSerializableEntryCollection<T>(Int32)](M_Tessa_Cards_CardSerializableEntryCollection_1__ctor_2.htm)|
Создаёт экземпляр класса с указанием начальной вместимости списка.  
[CardSerializableEntryCollection<T>(SerializationInfo,
StreamingContext)](M_Tessa_Cards_CardSerializableEntryCollection_1__ctor_3.htm)|
Создаёт экземпляр класса, десериализованный с использованием переданного
объекта [System.Runtime.Serialization.SerializationInfo].  
## __Свойства
[Count](P_Tessa_Cards_CardSerializableEntryCollection_1_Count.htm)| Количество
элементов в коллекции.  
---|---  
[IsReadOnly](P_Tessa_Cards_CardSerializableEntryCollection_1_IsReadOnly.htm)|
Признак доступности коллекции только для чтения.
Свойство возвращает значение свойства [Tessa.Platform.ISealable.IsSealed].  
[IsSealed](P_Tessa_Cards_CardSerializableObject_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[Item[Guid]](P_Tessa_Cards_CardSerializableEntryCollection_1_Item.htm)|
Возвращает элемент коллекции по его идентификатору.  
[Item[Int32]](P_Tessa_Cards_CardSerializableEntryCollection_1_Item_1.htm)|
Возвращает элемент коллекции по его индексу в списке.  
[Item[String]](P_Tessa_Cards_CardSerializableEntryCollection_1_Item_2.htm)|
Возвращает элемент коллекции по его имени.  
[Reference](P_Tessa_Cards_CardSerializableObject_Reference.htm)|  Имя
глобального объекта, на который ссылается данный объект.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[XmlElementNameInternal](P_Tessa_Cards_CardSerializableObject_XmlElementNameInternal.htm)|
Имя XML-элемента, для которого выполняется сериализация и десериализация.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[XmlItemNameInternal](P_Tessa_Cards_CardSerializableEntryCollection_1_XmlItemNameInternal.htm)|
Имя входящих в коллекцию XML-элементов, для которых выполняется сериализация и
десериализация.  
##  __Методы
[Add](M_Tessa_Cards_CardSerializableEntryCollection_1_Add.htm)| Добавляет
заданный элемент в коллекцию.  
---|---  
[CheckSealed](M_Tessa_Cards_CardSerializableObject_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[Clear](M_Tessa_Cards_CardSerializableEntryCollection_1_Clear.htm)| Удаляет
все элементы коллекции.  
[Contains(T)](M_Tessa_Cards_CardSerializableEntryCollection_1_Contains_2.htm)|
Возвращает признак того, что заданный элемент содержится в коллекции.  
[Contains(Guid)](M_Tessa_Cards_CardSerializableEntryCollection_1_Contains.htm)|
Возвращает признак того, что элемент с заданным идентификатором присутствует в
коллекции.  
[Contains(String)](M_Tessa_Cards_CardSerializableEntryCollection_1_Contains_1.htm)|
Возвращает признак того, что элемент с заданным именем присутствует в
коллекции.  
[CopyTo](M_Tessa_Cards_CardSerializableEntryCollection_1_CopyTo.htm)| Копирует
элементы коллекции в массив, начиная с заданного отсчитываемого от нуля
индекса.  
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
(Переопределяет
[CardSerializableObject.DeserializeChildrenFromBinaryInternal(BinaryReader)](M_Tessa_Cards_CardSerializableObject_DeserializeChildrenFromBinaryInternal.htm))  
[DeserializeElementFromXml](M_Tessa_Cards_CardSerializableEntryCollection_1_DeserializeElementFromXml.htm)|
Выполняется для каждого элемента десериализуемого объекта.  
(Переопределяет [CardSerializableObject.DeserializeElementFromXml(String,
XmlReader)](M_Tessa_Cards_CardSerializableObject_DeserializeElementFromXml.htm))  
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
[GetEnumerator](M_Tessa_Cards_CardSerializableEntryCollection_1_GetEnumerator.htm)|
Возвращает итератор по элементам коллекции.  
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
[Insert](M_Tessa_Cards_CardSerializableEntryCollection_1_Insert.htm)|
Вставляет элемент в заданную позицию.  
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
(Переопределяет
[CardSerializableObject.OnDeserializing(SerializationMode)](M_Tessa_Cards_CardSerializableObject_OnDeserializing.htm))  
[OnItemAttributeSerializationToXml](M_Tessa_Cards_CardSerializableEntryCollection_1_OnItemAttributeSerializationToXml.htm)|
Происходит перед сериализацией элементов коллекции в XML-элемент.
При переопределении метода в него можно добавить логику по дополнению XML-
элемента атрибутами, которые не были добавлены методом сериализации самого
элемента коллекции, но которые обрабатываются при десериализации XML-элемента.  
[Remove(T)](M_Tessa_Cards_CardSerializableEntryCollection_1_Remove_2.htm)|
Удаляет заданный элемент из коллекции.  
[Remove(Guid)](M_Tessa_Cards_CardSerializableEntryCollection_1_Remove.htm)|
Удаляет элемент с заданным идентификатором из коллекции.  
[Remove(String)](M_Tessa_Cards_CardSerializableEntryCollection_1_Remove_1.htm)|
Удаляет элемент с заданным именем из коллекции.  
[RemoveAt](M_Tessa_Cards_CardSerializableEntryCollection_1_RemoveAt.htm)|
Удаляет элемент в заданной позиции.  
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
(Переопределяет
[CardSchemeSerializableObject.RepairInternalAsync(ICardSchemeInfoProvider,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_CardSchemeSerializableObject_RepairInternalAsync.htm))  
[Seal](M_Tessa_Cards_CardSerializableObject_Seal.htm)| Защищает объект от
изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SealInternal](M_Tessa_Cards_CardSerializableEntryCollection_1_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Переопределяет
[CardSerializableObject.SealInternal()](M_Tessa_Cards_CardSerializableObject_SealInternal.htm))  
[SerializeAttributesToXml](M_Tessa_Cards_CardSerializableObject_SerializeAttributesToXml.htm)|
Выполняет сериализацию текущего объекта в атрибуты XML.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SerializeChildrenToBinaryInternal](M_Tessa_Cards_CardSerializableEntryCollection_1_SerializeChildrenToBinaryInternal.htm)|
Выполняет сериализацию всех дочерних объектов в байтовый поток.  
(Переопределяет
[CardSerializableObject.SerializeChildrenToBinaryInternal(BinaryWriter)](M_Tessa_Cards_CardSerializableObject_SerializeChildrenToBinaryInternal.htm))  
[SerializeElementsToXml](M_Tessa_Cards_CardSerializableEntryCollection_1_SerializeElementsToXml.htm)|
Выполняет сериализацию всех дочерних объектов для текущего объекта в элементы
XML.  
(Переопределяет
[CardSerializableObject.SerializeElementsToXml(XmlWriter)](M_Tessa_Cards_CardSerializableObject_SerializeElementsToXml.htm))  
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
[TryGetValue(String,
T)](M_Tessa_Cards_CardSerializableEntryCollection_1_TryGetValue_1.htm)|
Пытается вернуть элемент коллекции по его имени.  
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
(Переопределяет
[ValidationObject.ValidateInternal(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationObject_ValidateInternal.htm))  
##  __Методы расширения
[AddRange<T>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<T>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AddRangeForList](M_Tessa_Platform_Collections_Extensions_AddRangeForList.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AsArray<T>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[ConvertToListDictionaries<T>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<T>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[CopyAndAddRange<T>](M_Tessa_Cards_CardExtensions_CopyAndAddRange__1.htm)|
Копирует коллекцию сериализуемых объектов sourceItems и в конец коллекции
сериализуемых объектов targetItems. Устанавливает порядок следования объектов,
если объекты поддерживают
[ICardMetadataOrderable](T_Tessa_Cards_ICardMetadataOrderable.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[CopyAndInsert<T>](M_Tessa_Cards_CardExtensions_CopyAndInsert__1.htm)|
Копирует коллекцию сериализуемых объектов sourceItems и вставляет по индексу в
коллекцию сериализуемых объектов targetItems. Устанавливает порядок следования
объектов, если объекты поддерживают
[ICardMetadataOrderable](T_Tessa_Cards_ICardMetadataOrderable.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[CopyToTheBeginningOf<T>](M_Tessa_Cards_CardExtensions_CopyToTheBeginningOf__1.htm)|
Копирует коллекцию сериализуемых объектов sourceItems в начало коллекции
сериализуемых объектов targetItems. Устанавливает порядок следования объектов,
если объекты поддерживают
[ICardMetadataOrderable](T_Tessa_Cards_ICardMetadataOrderable.htm).  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[ForEach<T>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<T, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<T>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<T>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<T>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_2.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начиная с заданного индекса и заканчивая последним
элементом.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<T>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_3.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начинающемся с заданного индекса и содержащем указанное
число элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertRange<T>](M_Tessa_Platform_Collections_Extensions_InsertRange__1.htm)|
Вставляет диапазон элементов в заданный список items, начиная с указанного
индекса index.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertRangeForList](M_Tessa_Platform_Collections_Extensions_InsertRangeForList.htm)|
Вставляет диапазон элементов в заданный список items, начиная с указанного
индекса index.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertWithoutCopy<T>](M_Tessa_Cards_CardExtensions_InsertWithoutCopy__1.htm)|
Вставляет коллекцию сериализуемых объектов sourceItems по указанному индексу в
коллекцию сериализуемых объектов targetItems.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[LastIndexOf<T>](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[LastIndexOf<T>](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1_1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<T>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<T>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<T,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<T,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<T>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<T>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RemoveAll<T>](M_Tessa_Platform_Collections_Extensions_RemoveAll__1.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveAllForList](M_Tessa_Platform_Collections_Extensions_RemoveAllForList.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<T>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<T>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<T>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<T, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<T>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<T>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableObjectList<T>](M_Tessa_Platform_Collections_Extensions_ToSealableObjectList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm) и защищается от изменений при
активации защиты в списке.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<T>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<T>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
