# CardMetadataSection - класс
Содержит метаинформацию о секции.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class CardMetadataSection : CardSerializableEntry, 
    	ICardMetadataOrderable
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class CardMetadataSection
    	Inherits CardSerializableEntry
    	Implements ICardMetadataOrderable
C++ __Копировать
    [SerializableAttribute]
    public ref class CardMetadataSection sealed : public CardSerializableEntry, 
    	ICardMetadataOrderable
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type CardMetadataSection = 
        class
            inherit CardSerializableEntry
            interface ICardMetadataOrderable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm) __[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) __[CardSchemeSerializableObject](T_Tessa_Cards_CardSchemeSerializableObject.htm) __[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm) __ CardMetadataSection
Implements
    [ICardMetadataOrderable](T_Tessa_Cards_ICardMetadataOrderable.htm)
##  __Конструкторы
[CardMetadataSection()](M_Tessa_Cards_Metadata_CardMetadataSection__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[CardMetadataSection(CardMetadataSection,
IReadOnlyCollection<CardMetadataColumn>)](M_Tessa_Cards_Metadata_CardMetadataSection__ctor_2.htm)|
Создаёт экземпляр класса с указанием копируемого объекта и списка колонок.  
[CardMetadataSection(Guid, String, SchemeTableContentType, CardSectionType,
Int32, CardMetadataSectionFlags,
String)](M_Tessa_Cards_Metadata_CardMetadataSection__ctor_1.htm)|  Создаёт
экземпляр класса с указанием свойств секции.  
## __Свойства
[Columns](P_Tessa_Cards_Metadata_CardMetadataSection_Columns.htm)|  Колонки
секции.  
---|---  
[Flags](P_Tessa_Cards_Metadata_CardMetadataSection_Flags.htm)|  Флаги секции
карточки.  
[Group](P_Tessa_Cards_Metadata_CardMetadataSection_Group.htm)|  Наименование
группы к которой относится секция.  
[ID](P_Tessa_Cards_CardSerializableEntry_ID.htm)| Идентификатор объекта.  
(Унаследован от
[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm))  
[IsSealed](P_Tessa_Cards_CardSerializableObject_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[IsVirtual](P_Tessa_Cards_Metadata_CardMetadataSection_IsVirtual.htm)|
Получает или задаёт признак того, что секция является виртуальной. Значение
поля определяется флагом Virtual.  
[Name](P_Tessa_Cards_CardSerializableEntry_Name.htm)| Отображаемое имя
объекта.  
(Унаследован от
[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm))  
[Order](P_Tessa_Cards_Metadata_CardMetadataSection_Order.htm)|  Номер,
определяющий порядок сортировки секций при вставке данных в секции. При
удалении данных из секций порядок обратный.  
[Reference](P_Tessa_Cards_CardSerializableObject_Reference.htm)|  Имя
глобального объекта, на который ссылается данный объект.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SectionTableType](P_Tessa_Cards_Metadata_CardMetadataSection_SectionTableType.htm)|
Тип таблицы, указываемый в свойстве секции
[TableType](P_Tessa_Cards_CardSection_TableType.htm). Зависит от свойств
[SectionType](P_Tessa_Cards_Metadata_CardMetadataSection_SectionType.htm) и
[TableType](P_Tessa_Cards_Metadata_CardMetadataSection_TableType.htm). При
изменении значения этого свойства будут также изменены оба зависимых свойства,
причём значение [Unspecified](T_Tessa_Cards_CardTableType.htm) недопустимо в
качестве устанавливаемого.  
[SectionType](P_Tessa_Cards_Metadata_CardMetadataSection_SectionType.htm)|
Тип секции из перечисления
[CardSectionType](T_Tessa_Cards_CardSectionType.htm).  
[TableType](P_Tessa_Cards_Metadata_CardMetadataSection_TableType.htm)|  Тип
таблицы из перечисления
[SchemeTableContentType](T_Tessa_Scheme_SchemeTableContentType.htm).  
[XmlElementNameInternal](P_Tessa_Cards_Metadata_CardMetadataSection_XmlElementNameInternal.htm)|
Имя XML-элемента, для которого выполняется сериализация и десериализация.  
(Переопределяет
[CardSerializableObject.XmlElementNameInternal](P_Tessa_Cards_CardSerializableObject_XmlElementNameInternal.htm))  
##  __Методы
[CheckSealed](M_Tessa_Cards_CardSerializableObject_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
---|---  
[CreateAndEnsureSealing<T>](M_Tessa_Cards_CardSerializableObject_CreateAndEnsureSealing__1.htm)|
Создаёт объект типа T посредством конструктора по умолчанию и защищает его от
изменений, если текущий объект также защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DeserializeAttributeFromXml](M_Tessa_Cards_Metadata_CardMetadataSection_DeserializeAttributeFromXml.htm)|
Выполняется для каждого атрибута десериализуемого атрибута.  
(Переопределяет [CardSerializableEntry.DeserializeAttributeFromXml(String,
String)](M_Tessa_Cards_CardSerializableEntry_DeserializeAttributeFromXml.htm))  
[DeserializeChildrenFromBinaryInternal](M_Tessa_Cards_Metadata_CardMetadataSection_DeserializeChildrenFromBinaryInternal.htm)|
Выполняет десериализацию всех дочерних объектов из байтового потока.  
(Переопределяет
[CardSerializableObject.DeserializeChildrenFromBinaryInternal(BinaryReader)](M_Tessa_Cards_CardSerializableObject_DeserializeChildrenFromBinaryInternal.htm))  
[DeserializeElementFromXml](M_Tessa_Cards_Metadata_CardMetadataSection_DeserializeElementFromXml.htm)|
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
[DeserializeFromBinaryInternal](M_Tessa_Cards_Metadata_CardMetadataSection_DeserializeFromBinaryInternal.htm)|
Выполняет десериализацию всех полей текущего объекта из байтового потока.  
(Переопределяет
[CardSerializableEntry.DeserializeFromBinaryInternal(BinaryReader)](M_Tessa_Cards_CardSerializableEntry_DeserializeFromBinaryInternal.htm))  
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
[DeserializeFromStorageInternal](M_Tessa_Cards_Metadata_CardMetadataSection_DeserializeFromStorageInternal.htm)|
Выполняет десериализацию объекта и всех его дочерних объектов из хранилища
Dictionary<string, object>.  
(Переопределяет
[CardSerializableEntry.DeserializeFromStorageInternal(Dictionary<String,
Object>)](M_Tessa_Cards_CardSerializableEntry_DeserializeFromStorageInternal.htm))  
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
[Equals(ICardSerializableEntry)](M_Tessa_Cards_CardSerializableEntry_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
(Унаследован от
[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm))  
[Equals(Object)](M_Tessa_Cards_CardSerializableEntry_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Унаследован от
[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Cards_CardSerializableEntry_GetHashCode.htm)| Возвращает
хеш-код объекта.  
(Унаследован от
[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm))  
[GetObjectData](M_Tessa_Cards_CardSerializableObject_GetObjectData.htm)|
Записывает сериализованные данные текущего объекта в указанный объект
[System.Runtime.Serialization.SerializationInfo].  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[GetPhysicalReferenceNames](M_Tessa_Cards_Metadata_CardMetadataSection_GetPhysicalReferenceNames.htm)|
Возвращает имена физических колонок, которые являются ссылками на родительские
коллекционные или древовидные секции. Такие колонки указывают на RowID
родительских секций.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetValidationName](M_Tessa_Cards_CardSerializableEntry_GetValidationName.htm)|
Возвращает строку, определяющую имя объекта, или null, если имя объекта ещё
неизвестно или объект не содержит имени.  
(Унаследован от
[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm))  
[IDSpecified](M_Tessa_Cards_CardSerializableEntry_IDSpecified.htm)|
Возвращает признак того, что свойство
[ID](P_Tessa_Cards_CardSerializableEntry_ID.htm) было задано.  
(Унаследован от
[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm))  
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
[NameSpecified](M_Tessa_Cards_CardSerializableEntry_NameSpecified.htm)|
Возвращает признак того, что свойство
[Name](P_Tessa_Cards_CardSerializableEntry_Name.htm) было задано.  
(Унаследован от
[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm))  
[OnDeserialized](M_Tessa_Cards_CardSerializableObject_OnDeserialized.htm)|
Выполняется после успешной десериализации объекта и всех его дочерних объектов
из элемента XML.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[OnDeserializing](M_Tessa_Cards_Metadata_CardMetadataSection_OnDeserializing.htm)|
Выполняется перед десериализацией объекта и всех его дочерних объектов из
элемента XML.  
(Переопределяет
[CardSerializableEntry.OnDeserializing(SerializationMode)](M_Tessa_Cards_CardSerializableEntry_OnDeserializing.htm))  
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
[RepairInternalAsync](M_Tessa_Cards_Metadata_CardMetadataSection_RepairInternalAsync.htm)|
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
[SealInternal](M_Tessa_Cards_Metadata_CardMetadataSection_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Переопределяет
[CardSerializableObject.SealInternal()](M_Tessa_Cards_CardSerializableObject_SealInternal.htm))  
[SerializeAttributesToXml](M_Tessa_Cards_Metadata_CardMetadataSection_SerializeAttributesToXml.htm)|
Выполняет сериализацию текущего объекта в атрибуты XML.  
(Переопределяет
[CardSerializableEntry.SerializeAttributesToXml(XmlWriter)](M_Tessa_Cards_CardSerializableEntry_SerializeAttributesToXml.htm))  
[SerializeChildrenToBinaryInternal](M_Tessa_Cards_Metadata_CardMetadataSection_SerializeChildrenToBinaryInternal.htm)|
Выполняет сериализацию всех дочерних объектов в байтовый поток.  
(Переопределяет
[CardSerializableObject.SerializeChildrenToBinaryInternal(BinaryWriter)](M_Tessa_Cards_CardSerializableObject_SerializeChildrenToBinaryInternal.htm))  
[SerializeElementsToXml](M_Tessa_Cards_Metadata_CardMetadataSection_SerializeElementsToXml.htm)|
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
[SerializeToBinaryInternal](M_Tessa_Cards_Metadata_CardMetadataSection_SerializeToBinaryInternal.htm)|
Выполняет сериализацию текущего объекта в байтовый поток.  
(Переопределяет
[CardSerializableEntry.SerializeToBinaryInternal(BinaryWriter)](M_Tessa_Cards_CardSerializableEntry_SerializeToBinaryInternal.htm))  
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
[SerializeToStorageInternal](M_Tessa_Cards_Metadata_CardMetadataSection_SerializeToStorageInternal.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в
хранилище Dictionary<string, object>.  
(Переопределяет
[CardSerializableEntry.SerializeToStorageInternal(Dictionary<String,
Object>)](M_Tessa_Cards_CardSerializableEntry_SerializeToStorageInternal.htm))  
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
[ToString](M_Tessa_Cards_CardSerializableEntry_ToString.htm)| Возвращает
строковое представление объекта.  
(Унаследован от
[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm))  
[Validate()](M_Tessa_Platform_Validation_ValidationObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[ValidateInternal](M_Tessa_Cards_Metadata_CardMetadataSection_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Переопределяет
[CardSerializableEntry.ValidateInternal(IValidationResultBuilder)](M_Tessa_Cards_CardSerializableEntry_ValidateInternal.htm))  
##  __Поля
[XmlElementName](F_Tessa_Cards_Metadata_CardMetadataSection_XmlElementName.htm)|
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
##  __См. также
#### Ссылки
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
