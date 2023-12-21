# CardTypeTableControl - класс
Объект, описывающий расположение и свойства элемента управления для привязки к
колонкам коллекционной или древовидной секции карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class CardTypeTableControl : CardTypeControl
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class CardTypeTableControl
    	Inherits CardTypeControl
C++ __Копировать
    [SerializableAttribute]
    public ref class CardTypeTableControl sealed : public CardTypeControl
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type CardTypeTableControl = 
        class
            inherit CardTypeControl
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm) __[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) __[CardSchemeSerializableObject](T_Tessa_Cards_CardSchemeSerializableObject.htm) __[CardTypeContent](T_Tessa_Cards_CardTypeContent.htm) __[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm) __ CardTypeTableControl
##  __Конструкторы
[CardTypeTableControl](M_Tessa_Cards_CardTypeTableControl__ctor.htm)| Создаёт
экземпляр класса с параметрами по умолчанию.  
---|---  
##  __Свойства
[BlockSettings](P_Tessa_Cards_CardTypeControl_BlockSettings.htm)|  Настройки
блока [CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm), которые задаются для
каждого включённого в его состав объекта.  
(Унаследован от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm))  
---|---  
[Caption](P_Tessa_Cards_CardTypeContent_Caption.htm)|  Отображаемое имя
объекта.  
(Унаследован от [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm))  
[Columns](P_Tessa_Cards_CardTypeTableControl_Columns.htm)|  Объекты,
описывающие информацию о колонках коллекционных или древовидных секций
карточки.  
[ControlSettings](P_Tessa_Cards_CardTypeControl_ControlSettings.htm)|
Настройки используемого элемента управления, тип которого задан в свойстве
[Type](P_Tessa_Cards_CardTypeControl_Type.htm).  
(Унаследован от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm))  
[Flags](P_Tessa_Cards_CardTypeTableControl_Flags.htm)|  Флаги, определяющие
дополнительные атрибуты.  
[Form](P_Tessa_Cards_CardTypeTableControl_Form.htm)|  Объект, описывающий
пользовательский интерфейс для редактирования строки коллекционной или
древовидной секции.  
[IsSealed](P_Tessa_Cards_CardSerializableObject_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[Name](P_Tessa_Cards_CardTypeControl_Name.htm)|  Имя элемента управления или
null, если имя не задано. При задании пустой строки устанавливается значение
null. Рекомендуется задавать имя, уникальное для формы.  
(Унаследован от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm))  
[Order](P_Tessa_Cards_CardTypeContent_Order.htm)|  Порядок отображения объекта
в интерфейсе карточки.  
(Унаследован от [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm))  
[Reference](P_Tessa_Cards_CardSerializableObject_Reference.htm)|  Имя
глобального объекта, на который ссылается данный объект.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[RequiredText](P_Tessa_Cards_CardTypeTableControl_RequiredText.htm)|
Текст, отображаемый при отсутствии значения для контрола, значение которого
должно быть обязательно задано.
Если задано null или пустая строка, то используется строка из валидатора или
строка по умолчанию.  
[SectionID](P_Tessa_Cards_CardTypeTableControl_SectionID.htm)|  Идентификатор
секции.  
[ToolTip](P_Tessa_Cards_CardTypeControl_ToolTip.htm)|  Текст всплывающей
подсказки для элемента управления или null, если имя не задано. При задании
пустой строки или строки, состоящей из пробелов, устанавливается значение
null.  
(Унаследован от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm))  
[Type](P_Tessa_Cards_CardTypeControl_Type.htm)|  Тип используемого элемента
управления.  
(Унаследован от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm))  
[XmlElementNameInternal](P_Tessa_Cards_CardTypeTableControl_XmlElementNameInternal.htm)|
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
[DeserializeAttributeFromXml](M_Tessa_Cards_CardTypeTableControl_DeserializeAttributeFromXml.htm)|
Выполняется для каждого атрибута десериализуемого атрибута.  
(Переопределяет [CardTypeControl.DeserializeAttributeFromXml(String,
String)](M_Tessa_Cards_CardTypeControl_DeserializeAttributeFromXml.htm))  
[DeserializeChildrenFromBinaryInternal](M_Tessa_Cards_CardTypeTableControl_DeserializeChildrenFromBinaryInternal.htm)|
Выполняет десериализацию всех дочерних объектов из байтового потока.  
(Переопределяет
[CardSerializableObject.DeserializeChildrenFromBinaryInternal(BinaryReader)](M_Tessa_Cards_CardSerializableObject_DeserializeChildrenFromBinaryInternal.htm))  
[DeserializeElementFromXml](M_Tessa_Cards_CardTypeTableControl_DeserializeElementFromXml.htm)|
Выполняется для каждого элемента десериализуемого объекта.  
(Переопределяет [CardTypeControl.DeserializeElementFromXml(String,
XmlReader)](M_Tessa_Cards_CardTypeControl_DeserializeElementFromXml.htm))  
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
[DeserializeFromBinaryInternal](M_Tessa_Cards_CardTypeTableControl_DeserializeFromBinaryInternal.htm)|
Выполняет десериализацию всех полей текущего объекта из байтового потока.  
(Переопределяет
[CardTypeControl.DeserializeFromBinaryInternal(BinaryReader)](M_Tessa_Cards_CardTypeControl_DeserializeFromBinaryInternal.htm))  
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
[DeserializeFromStorageInternal](M_Tessa_Cards_CardTypeTableControl_DeserializeFromStorageInternal.htm)|
Выполняет десериализацию объекта и всех его дочерних объектов из хранилища
Dictionary<string, object>.  
(Переопределяет
[CardTypeControl.DeserializeFromStorageInternal(Dictionary<String,
Object>)](M_Tessa_Cards_CardTypeControl_DeserializeFromStorageInternal.htm))  
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
[Equals(CardTypeContent)](M_Tessa_Cards_CardTypeContent_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
(Унаследован от [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm))  
[Equals(Object)](M_Tessa_Cards_CardTypeContent_Equals.htm)| Сравнивает текущий
объект с заданным.  
(Унаследован от [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm))  
[EqualsByBlockSettings](M_Tessa_Cards_CardTypeControl_EqualsByBlockSettings.htm)|
Сравнивает сериализованные значения свойств
[BlockSettings](P_Tessa_Cards_CardTypeControl_BlockSettings.htm).  
(Унаследован от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm))  
[EqualsByControlSettings](M_Tessa_Cards_CardTypeControl_EqualsByControlSettings.htm)|
Сравнивает сериализованные значения свойств
[ControlSettings](P_Tessa_Cards_CardTypeControl_ControlSettings.htm).  
(Унаследован от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm))  
[EqualsInternal](M_Tessa_Cards_CardTypeTableControl_EqualsInternal.htm)|
Сравнивает заданный объект с текущим по всем полям.  
(Переопределяет
[CardTypeControl.EqualsInternal(CardTypeContent)](M_Tessa_Cards_CardTypeControl_EqualsInternal.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Cards_CardTypeContent_GetHashCode.htm)| Возвращает хеш-
код объекта.  
(Унаследован от [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm))  
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
[GetValidationName](M_Tessa_Cards_CardTypeContent_GetValidationName.htm)|
Возвращает строку, определяющую имя объекта, или null, если имя объекта ещё
неизвестно или объект не содержит имени.  
(Унаследован от [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm))  
[IsRequired](M_Tessa_Cards_CardTypeTableControl_IsRequired.htm)|  Возвращает
признак того, что значение, редактируемое элементом управления, является
обязательным для заполнения.  
(Переопределяет
[CardTypeControl.IsRequired()](M_Tessa_Cards_CardTypeControl_IsRequired.htm))  
[IsValid](M_Tessa_Platform_Validation_ValidationObject_IsValid.htm)| Выполняет
проверку объекта на валидность и возвращает признак того, что объект является
валидным.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[IsVisible](M_Tessa_Cards_CardTypeTableControl_IsVisible.htm)| Возвращает
признак того, что элемент управления является видимым в интерфейсе.  
(Переопределяет
[CardTypeControl.IsVisible()](M_Tessa_Cards_CardTypeControl_IsVisible.htm))  
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
[OnDeserializing](M_Tessa_Cards_CardTypeTableControl_OnDeserializing.htm)|
Выполняется перед десериализацией объекта и всех его дочерних объектов из
элемента XML.  
(Переопределяет
[CardTypeControl.OnDeserializing(SerializationMode)](M_Tessa_Cards_CardTypeControl_OnDeserializing.htm))  
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
[RepairInternalAsync](M_Tessa_Cards_CardTypeTableControl_RepairInternalAsync.htm)|
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
[SealInternal](M_Tessa_Cards_CardTypeTableControl_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Переопределяет
[CardTypeControl.SealInternal()](M_Tessa_Cards_CardTypeControl_SealInternal.htm))  
[SerializeAttributesToXml](M_Tessa_Cards_CardTypeTableControl_SerializeAttributesToXml.htm)|
Выполняет сериализацию текущего объекта в атрибуты XML.  
(Переопределяет
[CardTypeControl.SerializeAttributesToXml(XmlWriter)](M_Tessa_Cards_CardTypeControl_SerializeAttributesToXml.htm))  
[SerializeChildrenToBinaryInternal](M_Tessa_Cards_CardTypeTableControl_SerializeChildrenToBinaryInternal.htm)|
Выполняет сериализацию всех дочерних объектов в байтовый поток.  
(Переопределяет
[CardSerializableObject.SerializeChildrenToBinaryInternal(BinaryWriter)](M_Tessa_Cards_CardSerializableObject_SerializeChildrenToBinaryInternal.htm))  
[SerializeElementsToXml](M_Tessa_Cards_CardTypeTableControl_SerializeElementsToXml.htm)|
Выполняет сериализацию всех дочерних объектов для текущего объекта в элементы
XML.  
(Переопределяет
[CardTypeControl.SerializeElementsToXml(XmlWriter)](M_Tessa_Cards_CardTypeControl_SerializeElementsToXml.htm))  
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
[SerializeToBinaryInternal](M_Tessa_Cards_CardTypeTableControl_SerializeToBinaryInternal.htm)|
Выполняет сериализацию текущего объекта в байтовый поток.  
(Переопределяет
[CardTypeControl.SerializeToBinaryInternal(BinaryWriter)](M_Tessa_Cards_CardTypeControl_SerializeToBinaryInternal.htm))  
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
[SerializeToStorageInternal](M_Tessa_Cards_CardTypeTableControl_SerializeToStorageInternal.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в
хранилище Dictionary<string, object>.  
(Переопределяет [CardTypeControl.SerializeToStorageInternal(Dictionary<String,
Object>)](M_Tessa_Cards_CardTypeControl_SerializeToStorageInternal.htm))  
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
[SetRequired](M_Tessa_Cards_CardTypeTableControl_SetRequired.htm)|
Устанавливает признак того, что значение, редактируемое элементом управления,
является обязательным для заполнения. Если элемент управления не поддерживает
установку такого признака, то действий не выполняется.  
(Переопределяет
[CardTypeControl.SetRequired(Boolean)](M_Tessa_Cards_CardTypeControl_SetRequired.htm))  
[SetVisible](M_Tessa_Cards_CardTypeTableControl_SetVisible.htm)|
Устанавливает признак того, что элемент управления является видимым в
интерфейсе. Если элемент управления не поддерживает установку такого признака,
то действий не выполняется.  
(Переопределяет
[CardTypeControl.SetVisible(Boolean)](M_Tessa_Cards_CardTypeControl_SetVisible.htm))  
[ToString](M_Tessa_Cards_CardTypeContent_ToString.htm)| Возвращает строковое
представление объекта.  
(Унаследован от [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm))  
[Validate()](M_Tessa_Platform_Validation_ValidationObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[ValidateInternal](M_Tessa_Cards_CardTypeTableControl_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Переопределяет
[CardTypeContent.ValidateInternal(IValidationResultBuilder)](M_Tessa_Cards_CardTypeContent_ValidateInternal.htm))  
##  __Поля
[XmlElementName](F_Tessa_Cards_CardTypeTableControl_XmlElementName.htm)|  Имя
XML-элемента.  
---|---  
## __Методы расширения
[DeepClone](M_Tessa_Cards_CardExtensions_DeepClone.htm)|  Выполняет глубокое
клонирование метаинформации по элементу управления
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm) за счёт его полной
сериализации / десериализации.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[GetCaptionVisibility](M_Tessa_UI_Cards_CardUIExtensions_GetCaptionVisibility_1.htm)|
Возвращает отображаемое состояние для заголовка элемента управления, заданного
по указанной метаинформации.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[GetControlSpan](M_Tessa_UI_Cards_CardUIExtensions_GetControlSpan.htm)|
Возвращает отображаемое состояние для заголовка элемента управления, заданного
по указанной метаинформации.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[GetSourceInfo](M_Tessa_Cards_CardExtensions_GetSourceInfo.htm)|  Метод для
поулчения информации об источнике данных контрола с учетом возможной
регистрации кастомного метода для получения источника данных в
[ICardControlTypeRegistry](T_Tessa_Cards_ICardControlTypeRegistry.htm)  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[MakeGlobal](M_Tessa_Cards_CardExtensions_MakeGlobal_8.htm)|  Сделать
указанный объект глобальным.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
