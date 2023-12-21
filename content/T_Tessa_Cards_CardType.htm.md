# CardType - класс
Объект, описывающий тип карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class CardType : CardTypeTabForm, 
    	ICardSerializableEntry, INamedEntry, INamedItem, IEquatable<CardType>, 
    	IEquatable<CardTypeRepositoryData>
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class CardType
    	Inherits CardTypeTabForm
    	Implements ICardSerializableEntry, INamedEntry, INamedItem, IEquatable(Of CardType), 
    	IEquatable(Of CardTypeRepositoryData)
C++ __Копировать
    [SerializableAttribute]
    public ref class CardType sealed : public CardTypeTabForm, 
    	ICardSerializableEntry, INamedEntry, INamedItem, IEquatable<CardType^>, 
    	IEquatable<CardTypeRepositoryData^>
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type CardType = 
        class
            inherit CardTypeTabForm
            interface ICardSerializableEntry
            interface INamedEntry
            interface INamedItem
            interface IEquatable<CardType>
            interface IEquatable<CardTypeRepositoryData>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm) __[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) __[CardSchemeSerializableObject](T_Tessa_Cards_CardSchemeSerializableObject.htm) __[CardTypeForm](T_Tessa_Cards_CardTypeForm.htm) __[CardTypeTabForm](T_Tessa_Cards_CardTypeTabForm.htm) __ CardType
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<CardType>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[CardTypeRepositoryData](T_Tessa_Cards_CardTypeRepositoryData.htm)>, [ICardSerializableEntry](T_Tessa_Cards_ICardSerializableEntry.htm), [INamedItem](T_Tessa_Platform_Collections_INamedItem.htm), [INamedEntry](T_Tessa_Platform_INamedEntry.htm)
##  __Конструкторы
[CardType](M_Tessa_Cards_CardType__ctor.htm)| Создаёт экземпляр класса с
параметрами по умолчанию.  
---|---  
##  __Свойства
[Blocks](P_Tessa_Cards_CardTypeForm_Blocks.htm)|  Блоки типа карточки,
определяющие внешний вид карточки.  
(Унаследован от [CardTypeForm](T_Tessa_Cards_CardTypeForm.htm))  
---|---  
[Caption](P_Tessa_Cards_CardType_Caption.htm)|  Отображаемое имя типа
карточки.  
[CardTypeSections](P_Tessa_Cards_CardType_CardTypeSections.htm)|  Виртуальные
секции, которые доступны в пределах данного типа карточки.  
[CompletionOptions](P_Tessa_Cards_CardType_CompletionOptions.htm)|  Варианты
завершения типа карточки задания.  
[DigestFormat](P_Tessa_Cards_CardType_DigestFormat.htm)|  Формат функции
Digest для карточки. Актуально только для типов
[Card](T_Tessa_Cards_CardInstanceType.htm). Чтобы определить, действительно ли
строка содержит строку формата, можно использовать метод
[HasDigestFormat()](M_Tessa_Cards_CardType_HasDigestFormat.htm).  
[Extensions](P_Tessa_Cards_CardType_Extensions.htm)|  Список расширений для
типов карточек.  
[Flags](P_Tessa_Cards_CardType_Flags.htm)|  Флаги типа карточки.  
[FormClass](P_Tessa_Cards_CardTypeForm_FormClass.htm)|  Полное имя типа для
класса, выполняющего отображение формы карточки в UI.  
(Унаследован от [CardTypeForm](T_Tessa_Cards_CardTypeForm.htm))  
[Forms](P_Tessa_Cards_CardType_Forms.htm)|  Альтернативные варианты
пользовательского интерфейса для редактирования карточки.  
[FormSettings](P_Tessa_Cards_CardTypeForm_FormSettings.htm)|  Настройки
класса, полное имя типа которого задано в свойстве
[FormClass](P_Tessa_Cards_CardTypeForm_FormClass.htm).  
(Унаследован от [CardTypeForm](T_Tessa_Cards_CardTypeForm.htm))  
[Group](P_Tessa_Cards_CardType_Group.htm)|  Название группы для типа карточки.
Может быть равно null, если группа не задана.  
[ID](P_Tessa_Cards_CardType_ID.htm)| Идентификатор объекта.  
[InstanceType](P_Tessa_Cards_CardType_InstanceType.htm)|  Тип экземпляра
карточки.  
[IsSealed](P_Tessa_Cards_CardSerializableObject_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[Name](P_Tessa_Cards_CardType_Name.htm)| Отображаемое имя объекта.  
(Переопределяет
[CardTypeTabForm.Name](P_Tessa_Cards_CardTypeTabForm_Name.htm))  
[Reference](P_Tessa_Cards_CardSerializableObject_Reference.htm)|  Имя
глобального объекта, на который ссылается данный объект.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SchemeItems](P_Tessa_Cards_CardType_SchemeItems.htm)|  Метаданные всех
секций, входящих в состав типа карточки.  
[TabCaption](P_Tessa_Cards_CardTypeTabForm_TabCaption.htm)|  Заголовок вкладки
с формой.  
(Унаследован от [CardTypeTabForm](T_Tessa_Cards_CardTypeTabForm.htm))  
[TabOrder](P_Tessa_Cards_CardTypeTabForm_TabOrder.htm)|  Порядковый номер
вкладки с формой. Вкладки упорядочиваются по возрастанию номера.  
(Унаследован от [CardTypeTabForm](T_Tessa_Cards_CardTypeTabForm.htm))  
[Validators](P_Tessa_Cards_CardType_Validators.htm)|  Список валидаторов,
используемых при сохранении карточки.  
[XmlElementNameInternal](P_Tessa_Cards_CardType_XmlElementNameInternal.htm)|
Имя XML-элемента, для которого выполняется сериализация и десериализация.  
(Переопределяет
[CardSerializableObject.XmlElementNameInternal](P_Tessa_Cards_CardSerializableObject_XmlElementNameInternal.htm))  
##  __Методы
[BaseIsEmpty](M_Tessa_Cards_CardTypeTabForm_BaseIsEmpty.htm)| Возвращает
признак того, что базовый класс не содержит сериализуемой информации.  
(Унаследован от [CardTypeTabForm](T_Tessa_Cards_CardTypeTabForm.htm))  
---|---  
[CheckSealed](M_Tessa_Cards_CardSerializableObject_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[CreateAndEnsureSealing<T>](M_Tessa_Cards_CardSerializableObject_CreateAndEnsureSealing__1.htm)|
Создаёт объект типа T посредством конструктора по умолчанию и защищает его от
изменений, если текущий объект также защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DepthFirstVisitAsync](M_Tessa_Cards_CardType_DepthFirstVisitAsync.htm)|
Выполняет посещение всех объектов текущего типа карточки в порядке, начиная с
наименее вложенных объектов.  
[DeserializeAttributeFromXml](M_Tessa_Cards_CardType_DeserializeAttributeFromXml.htm)|
Выполняется для каждого атрибута десериализуемого атрибута.  
(Переопределяет [CardTypeTabForm.DeserializeAttributeFromXml(String,
String)](M_Tessa_Cards_CardTypeTabForm_DeserializeAttributeFromXml.htm))  
[DeserializeChildrenFromBinaryInternal](M_Tessa_Cards_CardType_DeserializeChildrenFromBinaryInternal.htm)|
Выполняет десериализацию всех дочерних объектов из байтового потока.  
(Переопределяет
[CardTypeForm.DeserializeChildrenFromBinaryInternal(BinaryReader)](M_Tessa_Cards_CardTypeForm_DeserializeChildrenFromBinaryInternal.htm))  
[DeserializeElementFromXml](M_Tessa_Cards_CardType_DeserializeElementFromXml.htm)|
Выполняется для каждого элемента десериализуемого объекта.  
(Переопределяет [CardTypeForm.DeserializeElementFromXml(String,
XmlReader)](M_Tessa_Cards_CardTypeForm_DeserializeElementFromXml.htm))  
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
[DeserializeFromBinaryInternal](M_Tessa_Cards_CardType_DeserializeFromBinaryInternal.htm)|
Выполняет десериализацию всех полей текущего объекта из байтового потока.  
(Переопределяет
[CardTypeTabForm.DeserializeFromBinaryInternal(BinaryReader)](M_Tessa_Cards_CardTypeTabForm_DeserializeFromBinaryInternal.htm))  
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
[DeserializeFromStorageInternal](M_Tessa_Cards_CardType_DeserializeFromStorageInternal.htm)|
Выполняет десериализацию объекта и всех его дочерних объектов из хранилища
Dictionary<string, object>.  
(Переопределяет
[CardTypeTabForm.DeserializeFromStorageInternal(Dictionary<String,
Object>)](M_Tessa_Cards_CardTypeTabForm_DeserializeFromStorageInternal.htm))  
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
[Equals(CardType)](M_Tessa_Cards_CardType_Equals_1.htm)| Сравнивает текущий
объект с заданным.  
[Equals(CardTypeRepositoryData)](M_Tessa_Cards_CardType_Equals_2.htm)|
Сравнивает текущий объект с заданным.  
[Equals(Object)](M_Tessa_Cards_CardType_Equals.htm)| Сравнивает текущий объект
с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[EqualsByFormSettings](M_Tessa_Cards_CardTypeForm_EqualsByFormSettings.htm)|
Сравнивает сериализованные значения свойств
[FormSettings](P_Tessa_Cards_CardTypeForm_FormSettings.htm).  
(Унаследован от [CardTypeForm](T_Tessa_Cards_CardTypeForm.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FormIsEmpty](M_Tessa_Cards_CardTypeForm_FormIsEmpty.htm)|  Возвращает признак
того, что форма не содержит отображаемых блоков.  
(Унаследован от [CardTypeForm](T_Tessa_Cards_CardTypeForm.htm))  
[GetHashCode](M_Tessa_Cards_CardType_GetHashCode.htm)| Возвращает хеш-код
объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[GetValidationName](M_Tessa_Cards_CardType_GetValidationName.htm)|  Возвращает
строку, определяющую имя объекта, или null, если имя объекта ещё неизвестно
или объект не содержит имени.  
(Переопределяет
[CardTypeTabForm.GetValidationName()](M_Tessa_Cards_CardTypeTabForm_GetValidationName.htm))  
[HasDigestFormat](M_Tessa_Cards_CardType_HasDigestFormat.htm)|  Возвращает
признак того, что свойство
[DigestFormat](P_Tessa_Cards_CardType_DigestFormat.htm) действительно содержит
строку формата, которая не является пробелами, пустой строкой или null.  
[IDSpecified](M_Tessa_Cards_CardType_IDSpecified.htm)|  Возвращает признак
того, что свойство [ID](P_Tessa_Cards_CardType_ID.htm) было задано.  
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
[NameSpecified](M_Tessa_Cards_CardType_NameSpecified.htm)|  Возвращает признак
того, что свойство [Name](P_Tessa_Cards_CardType_Name.htm) было задано.  
[OnDeserialized](M_Tessa_Cards_CardSerializableObject_OnDeserialized.htm)|
Выполняется после успешной десериализации объекта и всех его дочерних объектов
из элемента XML.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[OnDeserializing](M_Tessa_Cards_CardType_OnDeserializing.htm)| Выполняется
перед десериализацией объекта и всех его дочерних объектов из элемента XML.  
(Переопределяет
[CardTypeTabForm.OnDeserializing(SerializationMode)](M_Tessa_Cards_CardTypeTabForm_OnDeserializing.htm))  
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
[RepairInternalAsync](M_Tessa_Cards_CardType_RepairInternalAsync.htm)|  Метод
восстанавливает объект к работоспособному состоянии в соответствии со схемой.
Этот процесс включает удаление данных из текущего объекта, которые имеют
отношение к схеме, но фактически в ней отсутствуют.  
(Переопределяет [CardTypeForm.RepairInternalAsync(ICardSchemeInfoProvider,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_CardTypeForm_RepairInternalAsync.htm))  
[Seal](M_Tessa_Cards_CardSerializableObject_Seal.htm)| Защищает объект от
изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SealInternal](M_Tessa_Cards_CardType_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Переопределяет
[CardTypeForm.SealInternal()](M_Tessa_Cards_CardTypeForm_SealInternal.htm))  
[SerializeAttributesToXml](M_Tessa_Cards_CardType_SerializeAttributesToXml.htm)|
Выполняет сериализацию текущего объекта в атрибуты XML.  
(Переопределяет
[CardTypeTabForm.SerializeAttributesToXml(XmlWriter)](M_Tessa_Cards_CardTypeTabForm_SerializeAttributesToXml.htm))  
[SerializeChildrenToBinaryInternal](M_Tessa_Cards_CardType_SerializeChildrenToBinaryInternal.htm)|
Выполняет сериализацию всех дочерних объектов в байтовый поток.  
(Переопределяет
[CardTypeForm.SerializeChildrenToBinaryInternal(BinaryWriter)](M_Tessa_Cards_CardTypeForm_SerializeChildrenToBinaryInternal.htm))  
[SerializeElementsToXml](M_Tessa_Cards_CardType_SerializeElementsToXml.htm)|
Выполняет сериализацию всех дочерних объектов для текущего объекта в элементы
XML.  
(Переопределяет
[CardTypeForm.SerializeElementsToXml(XmlWriter)](M_Tessa_Cards_CardTypeForm_SerializeElementsToXml.htm))  
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
[SerializeToBinaryInternal](M_Tessa_Cards_CardType_SerializeToBinaryInternal.htm)|
Выполняет сериализацию текущего объекта в байтовый поток.  
(Переопределяет
[CardTypeTabForm.SerializeToBinaryInternal(BinaryWriter)](M_Tessa_Cards_CardTypeTabForm_SerializeToBinaryInternal.htm))  
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
[SerializeToStorageInternal](M_Tessa_Cards_CardType_SerializeToStorageInternal.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в
хранилище Dictionary<string, object>.  
(Переопределяет [CardTypeTabForm.SerializeToStorageInternal(Dictionary<String,
Object>)](M_Tessa_Cards_CardTypeTabForm_SerializeToStorageInternal.htm))  
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
[ToRepositoryData](M_Tessa_Cards_CardType_ToRepositoryData.htm)|  Возвращает
объект [CardTypeRepositoryData](T_Tessa_Cards_CardTypeRepositoryData.htm),
описывающий тип карточки в форме, пригодной для хранения в базе данных.  
[ToString](M_Tessa_Cards_CardType_ToString.htm)| Возвращает строковое
представление объекта.  
(Переопределяет
[CardTypeTabForm.ToString()](M_Tessa_Cards_CardTypeTabForm_ToString.htm))  
[TryGetCompletionOptionValidators](M_Tessa_Cards_CardType_TryGetCompletionOptionValidators.htm)|
Возвращает список валидаторов, связанных с вариантом завершения, подходящего
для заданной формы задания, или null, если текущий тип не является типом
задания, или с формой не связано ни одного или связано более одного варианта
завершения.  
[Validate()](M_Tessa_Platform_Validation_ValidationObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[ValidateInternal](M_Tessa_Cards_CardType_ValidateInternal.htm)| Выполняет
валидацию текущего объекта и всех его дочерних объектов.  
(Переопределяет
[CardTypeForm.ValidateInternal(IValidationResultBuilder)](M_Tessa_Cards_CardTypeForm_ValidateInternal.htm))  
[VisitAsync](M_Tessa_Cards_CardType_VisitAsync.htm)|  Выполняет посещение всех
объектов текущего типа карточки в порядке, начиная с наиболее вложенных
объектов.  
## __Поля
[XmlElementName](F_Tessa_Cards_CardType_XmlElementName.htm)|  Имя XML-
элемента.  
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
[IsTopLevelForm](M_Tessa_UI_Cards_CardUIExtensions_IsTopLevelForm.htm)|
Возвращает признак того, что форма является формой верхнего уровня карточки,
т.е. это не форма дочерних элементов управления.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[ReplaceBlocks](M_Tessa_Cards_CardExtensions_ReplaceBlocks_1.htm)|  Заменить
блоки формы на блоки исходной формы.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
