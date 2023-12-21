# CardTypeSchemeItem - класс
Метаданные секции, которая входит в состав типа карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class CardTypeSchemeItem : CardSchemeSerializableObject, 
    	IEquatable<CardTypeSchemeItem>
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class CardTypeSchemeItem
    	Inherits CardSchemeSerializableObject
    	Implements IEquatable(Of CardTypeSchemeItem)
C++ __Копировать
    [SerializableAttribute]
    public ref class CardTypeSchemeItem sealed : public CardSchemeSerializableObject, 
    	IEquatable<CardTypeSchemeItem^>
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type CardTypeSchemeItem = 
        class
            inherit CardSchemeSerializableObject
            interface IEquatable<CardTypeSchemeItem>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm) __[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) __[CardSchemeSerializableObject](T_Tessa_Cards_CardSchemeSerializableObject.htm) __ CardTypeSchemeItem
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<CardTypeSchemeItem>
##  __Конструкторы
[CardTypeSchemeItem](M_Tessa_Cards_CardTypeSchemeItem__ctor.htm)| Создаёт
экземпляр класса с параметрами по умолчанию.  
---|---  
##  __Свойства
[ColumnIDList](P_Tessa_Cards_CardTypeSchemeItem_ColumnIDList.htm)|  Список
идентификаторов физических и комплексных колонок секции
[SectionID](P_Tessa_Cards_CardTypeSchemeItem_SectionID.htm), которые
определяют, какие колонки будут загружаться для типа карточки.  
---|---  
[IsSealed](P_Tessa_Cards_CardSerializableObject_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[Reference](P_Tessa_Cards_CardSerializableObject_Reference.htm)|  Имя
глобального объекта, на который ссылается данный объект.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SectionID](P_Tessa_Cards_CardTypeSchemeItem_SectionID.htm)|  Идентификатор
секции, в которой содержится колонки с заданным идентификаторами
[ColumnIDList](P_Tessa_Cards_CardTypeSchemeItem_ColumnIDList.htm), или null,
если поле содержится в физической колонке или составлено из нескольких
физических колонок.  
[XmlElementNameInternal](P_Tessa_Cards_CardTypeSchemeItem_XmlElementNameInternal.htm)|
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
[DeserializeAttributeFromXml](M_Tessa_Cards_CardTypeSchemeItem_DeserializeAttributeFromXml.htm)|
Выполняется для каждого атрибута десериализуемого атрибута.  
(Переопределяет [CardSerializableObject.DeserializeAttributeFromXml(String,
String)](M_Tessa_Cards_CardSerializableObject_DeserializeAttributeFromXml.htm))  
[DeserializeChildrenFromBinaryInternal](M_Tessa_Cards_CardSerializableObject_DeserializeChildrenFromBinaryInternal.htm)|
Выполняет десериализацию всех дочерних объектов из байтового потока.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[DeserializeElementFromXml](M_Tessa_Cards_CardSerializableObject_DeserializeElementFromXml.htm)|
Выполняется для каждого элемента десериализуемого объекта.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
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
[DeserializeFromBinaryInternal](M_Tessa_Cards_CardTypeSchemeItem_DeserializeFromBinaryInternal.htm)|
Выполняет десериализацию всех полей текущего объекта из байтового потока.  
(Переопределяет
[CardSerializableObject.DeserializeFromBinaryInternal(BinaryReader)](M_Tessa_Cards_CardSerializableObject_DeserializeFromBinaryInternal.htm))  
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
[DeserializeFromStorageInternal](M_Tessa_Cards_CardTypeSchemeItem_DeserializeFromStorageInternal.htm)|
Выполняет десериализацию объекта и всех его дочерних объектов из хранилища
Dictionary<string, object>.  
(Переопределяет
[CardSerializableObject.DeserializeFromStorageInternal(Dictionary<String,
Object>)](M_Tessa_Cards_CardSerializableObject_DeserializeFromStorageInternal.htm))  
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
[Equals(CardTypeSchemeItem)](M_Tessa_Cards_CardTypeSchemeItem_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
[Equals(Object)](M_Tessa_Cards_CardTypeSchemeItem_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Cards_CardTypeSchemeItem_GetHashCode.htm)| Возвращает
хеш-код объекта.  
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
[GetValidationName](M_Tessa_Cards_CardTypeSchemeItem_GetValidationName.htm)|
Возвращает строку, определяющую имя объекта, или null, если имя объекта ещё
неизвестно или объект не содержит имени.  
(Переопределяет
[ValidationObject.GetValidationName()](M_Tessa_Platform_Validation_ValidationObject_GetValidationName.htm))  
[IsEmpty](M_Tessa_Cards_CardTypeSchemeItem_IsEmpty.htm)|  Возвращает признак
того, что объект не содержит данных.  
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
[OnDeserializing](M_Tessa_Cards_CardTypeSchemeItem_OnDeserializing.htm)|
Выполняется перед десериализацией объекта и всех его дочерних объектов из
элемента XML.  
(Переопределяет
[CardSerializableObject.OnDeserializing(SerializationMode)](M_Tessa_Cards_CardSerializableObject_OnDeserializing.htm))  
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
[RepairInternalAsync](M_Tessa_Cards_CardTypeSchemeItem_RepairInternalAsync.htm)|
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
[SealInternal](M_Tessa_Cards_CardTypeSchemeItem_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Переопределяет
[CardSerializableObject.SealInternal()](M_Tessa_Cards_CardSerializableObject_SealInternal.htm))  
[SerializeAttributesToXml](M_Tessa_Cards_CardTypeSchemeItem_SerializeAttributesToXml.htm)|
Выполняет сериализацию текущего объекта в атрибуты XML.  
(Переопределяет
[CardSerializableObject.SerializeAttributesToXml(XmlWriter)](M_Tessa_Cards_CardSerializableObject_SerializeAttributesToXml.htm))  
[SerializeChildrenToBinaryInternal](M_Tessa_Cards_CardSerializableObject_SerializeChildrenToBinaryInternal.htm)|
Выполняет сериализацию всех дочерних объектов в байтовый поток.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SerializeElementsToXml](M_Tessa_Cards_CardSerializableObject_SerializeElementsToXml.htm)|
Выполняет сериализацию всех дочерних объектов для текущего объекта в элементы
XML.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
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
[SerializeToBinaryInternal](M_Tessa_Cards_CardTypeSchemeItem_SerializeToBinaryInternal.htm)|
Выполняет сериализацию текущего объекта в байтовый поток.  
(Переопределяет
[CardSerializableObject.SerializeToBinaryInternal(BinaryWriter)](M_Tessa_Cards_CardSerializableObject_SerializeToBinaryInternal.htm))  
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
[SerializeToStorageInternal](M_Tessa_Cards_CardTypeSchemeItem_SerializeToStorageInternal.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в
хранилище Dictionary<string, object>.  
(Переопределяет
[CardSerializableObject.SerializeToStorageInternal(Dictionary<String,
Object>)](M_Tessa_Cards_CardSerializableObject_SerializeToStorageInternal.htm))  
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
[Validate()](M_Tessa_Platform_Validation_ValidationObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[ValidateInternal](M_Tessa_Cards_CardTypeSchemeItem_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Переопределяет
[ValidationObject.ValidateInternal(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationObject_ValidateInternal.htm))  
##  __Поля
[XmlElementName](F_Tessa_Cards_CardTypeSchemeItem_XmlElementName.htm)|  Имя
XML-элемента.  
---|---  
## __Методы расширения
[AddCardTypeInfoToSections](M_Tessa_Cards_CardExtensions_AddCardTypeInfoToSections.htm)|
Добавляет информацию по типу карточки cardTypeID для колонок в метаинформации
sections, которые перечислены в schemeItem, если этого типа ещё нет в
соответствующих колонках. Возвращает признак того, что метод внёс изменения в
метаинформацию.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
