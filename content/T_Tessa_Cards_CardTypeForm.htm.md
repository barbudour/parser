# CardTypeForm - класс
Объект, описывающий базовую информацию о форме карточки. Тип карточки
[CardType](T_Tessa_Cards_CardType.htm) \- это частный случай формы.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public abstract class CardTypeForm : CardSchemeSerializableObject
VB __Копировать
    <SerializableAttribute>
    Public MustInherit Class CardTypeForm
    	Inherits CardSchemeSerializableObject
C++ __Копировать
    [SerializableAttribute]
    public ref class CardTypeForm abstract : public CardSchemeSerializableObject
F# __Копировать
     [<AbstractClassAttribute>]
    [<SerializableAttribute>]
    type CardTypeForm = 
        class
            inherit CardSchemeSerializableObject
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm) __[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) __[CardSchemeSerializableObject](T_Tessa_Cards_CardSchemeSerializableObject.htm) __ CardTypeForm
Derived
[Tessa.Cards.CardTypeTabForm](T_Tessa_Cards_CardTypeTabForm.htm)
[Tessa.Cards.CardTypeTableForm](T_Tessa_Cards_CardTypeTableForm.htm)
##  __Конструкторы
[CardTypeForm()](M_Tessa_Cards_CardTypeForm__ctor.htm)| Создаёт экземпляр
класса с параметрами по умолчанию.  
---|---  
[CardTypeForm(SerializationInfo,
StreamingContext)](M_Tessa_Cards_CardTypeForm__ctor_1.htm)|  Создаёт экземпляр
класса, десериализованный с использованием переданного объекта
[System.Runtime.Serialization.SerializationInfo].  
## __Свойства
[Blocks](P_Tessa_Cards_CardTypeForm_Blocks.htm)|  Блоки типа карточки,
определяющие внешний вид карточки.  
---|---  
[FormClass](P_Tessa_Cards_CardTypeForm_FormClass.htm)|  Полное имя типа для
класса, выполняющего отображение формы карточки в UI.  
[FormSettings](P_Tessa_Cards_CardTypeForm_FormSettings.htm)|  Настройки
класса, полное имя типа которого задано в свойстве
[FormClass](P_Tessa_Cards_CardTypeForm_FormClass.htm).  
[IsSealed](P_Tessa_Cards_CardSerializableObject_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[Reference](P_Tessa_Cards_CardSerializableObject_Reference.htm)|  Имя
глобального объекта, на который ссылается данный объект.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[XmlElementNameInternal](P_Tessa_Cards_CardSerializableObject_XmlElementNameInternal.htm)|
Имя XML-элемента, для которого выполняется сериализация и десериализация.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
##  __Методы
[BaseIsEmpty](M_Tessa_Cards_CardTypeForm_BaseIsEmpty.htm)| Возвращает признак
того, что базовый класс не содержит сериализуемой информации.  
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
[DeserializeAttributeFromXml](M_Tessa_Cards_CardTypeForm_DeserializeAttributeFromXml.htm)|
Выполняется для каждого атрибута десериализуемого атрибута.  
(Переопределяет [CardSerializableObject.DeserializeAttributeFromXml(String,
String)](M_Tessa_Cards_CardSerializableObject_DeserializeAttributeFromXml.htm))  
[DeserializeChildrenFromBinaryInternal](M_Tessa_Cards_CardTypeForm_DeserializeChildrenFromBinaryInternal.htm)|
Выполняет десериализацию всех дочерних объектов из байтового потока.  
(Переопределяет
[CardSerializableObject.DeserializeChildrenFromBinaryInternal(BinaryReader)](M_Tessa_Cards_CardSerializableObject_DeserializeChildrenFromBinaryInternal.htm))  
[DeserializeElementFromXml](M_Tessa_Cards_CardTypeForm_DeserializeElementFromXml.htm)|
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
[DeserializeFromBinaryInternal](M_Tessa_Cards_CardTypeForm_DeserializeFromBinaryInternal.htm)|
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
[DeserializeFromStorageInternal](M_Tessa_Cards_CardTypeForm_DeserializeFromStorageInternal.htm)|
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
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[EqualsByFormSettings](M_Tessa_Cards_CardTypeForm_EqualsByFormSettings.htm)|
Сравнивает сериализованные значения свойств
[FormSettings](P_Tessa_Cards_CardTypeForm_FormSettings.htm).  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FormIsEmpty](M_Tessa_Cards_CardTypeForm_FormIsEmpty.htm)|  Возвращает признак
того, что форма не содержит отображаемых блоков.  
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
[GetValidationName](M_Tessa_Cards_CardTypeForm_GetValidationName.htm)|
Возвращает строку, определяющую имя объекта, или null, если имя объекта ещё
неизвестно или объект не содержит имени.  
(Переопределяет
[ValidationObject.GetValidationName()](M_Tessa_Platform_Validation_ValidationObject_GetValidationName.htm))  
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
[OnDeserializing](M_Tessa_Cards_CardTypeForm_OnDeserializing.htm)| Выполняется
перед десериализацией объекта и всех его дочерних объектов из элемента XML.  
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
[RepairInternalAsync](M_Tessa_Cards_CardTypeForm_RepairInternalAsync.htm)|
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
[SealInternal](M_Tessa_Cards_CardTypeForm_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Переопределяет
[CardSerializableObject.SealInternal()](M_Tessa_Cards_CardSerializableObject_SealInternal.htm))  
[SerializeAttributesToXml](M_Tessa_Cards_CardTypeForm_SerializeAttributesToXml.htm)|
Выполняет сериализацию текущего объекта в атрибуты XML.  
(Переопределяет
[CardSerializableObject.SerializeAttributesToXml(XmlWriter)](M_Tessa_Cards_CardSerializableObject_SerializeAttributesToXml.htm))  
[SerializeChildrenToBinaryInternal](M_Tessa_Cards_CardTypeForm_SerializeChildrenToBinaryInternal.htm)|
Выполняет сериализацию всех дочерних объектов в байтовый поток.  
(Переопределяет
[CardSerializableObject.SerializeChildrenToBinaryInternal(BinaryWriter)](M_Tessa_Cards_CardSerializableObject_SerializeChildrenToBinaryInternal.htm))  
[SerializeElementsToXml](M_Tessa_Cards_CardTypeForm_SerializeElementsToXml.htm)|
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
[SerializeToBinaryInternal](M_Tessa_Cards_CardTypeForm_SerializeToBinaryInternal.htm)|
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
[SerializeToStorageInternal](M_Tessa_Cards_CardTypeForm_SerializeToStorageInternal.htm)|
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
[ValidateInternal](M_Tessa_Cards_CardTypeForm_ValidateInternal.htm)| Выполняет
валидацию текущего объекта и всех его дочерних объектов.  
(Переопределяет
[ValidationObject.ValidateInternal(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationObject_ValidateInternal.htm))  
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
