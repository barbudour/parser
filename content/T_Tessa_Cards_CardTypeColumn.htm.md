# CardTypeColumn - класс
Объект, описывающий колонку коллекционной или древовидной секции карточки
[CardTypeTableControl](T_Tessa_Cards_CardTypeTableControl.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class CardTypeColumn : CardTypeContent
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class CardTypeColumn
    	Inherits CardTypeContent
C++ __Копировать
    [SerializableAttribute]
    public ref class CardTypeColumn sealed : public CardTypeContent
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type CardTypeColumn = 
        class
            inherit CardTypeContent
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm) __[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) __[CardSchemeSerializableObject](T_Tessa_Cards_CardSchemeSerializableObject.htm) __[CardTypeContent](T_Tessa_Cards_CardTypeContent.htm) __ CardTypeColumn
##  __Конструкторы
[CardTypeColumn](M_Tessa_Cards_CardTypeColumn__ctor.htm)| Создаёт экземпляр
класса с параметрами по умолчанию.  
---|---  
##  __Свойства
[AggregationFormat](P_Tessa_Cards_CardTypeColumn_AggregationFormat.htm)|
Формат агрегации дочерних строк. Если значение равно null, то строки выводятся
как есть. Если количество дочерних строк равно нулю, то результирующая строка
должна быть равна null. В противном случае соединённые сепараторами
[Separator](P_Tessa_Cards_CardTypeColumn_Separator.htm) дочерние строки
приходят в качестве параметра {0}, а количество строк - в параметре {1}. Таким
образом, например, можно поставить точку в конце списка строк, разделённые
запятыми.  
---|---  
[Alignment](P_Tessa_Cards_CardTypeColumn_Alignment.htm)|  Выравнивание
содержимого, отображаемого в колонке.  
[Caption](P_Tessa_Cards_CardTypeContent_Caption.htm)|  Отображаемое имя
объекта.  
(Унаследован от [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm))  
[ComplexColumnID](P_Tessa_Cards_CardTypeColumn_ComplexColumnID.htm)|
Идентификатор комплексной колонки, в которой содержится значение поля, или
null, если поле содержится в физической колонке или составлено из нескольких
физических колонок.  
[DisplayFormat](P_Tessa_Cards_CardTypeColumn_DisplayFormat.htm)|  Формат
отображаемых в текстовом виде полей колонки. Если задано null или пустая
строка, то в текстовом виде поле будет отображаться как значение комплексной
колонки [ComplexColumnID](P_Tessa_Cards_CardTypeColumn_ComplexColumnID.htm)
или первой колонки из списка
[PhysicalColumnIDList](P_Tessa_Cards_CardTypeColumn_PhysicalColumnIDList.htm).  
[Flags](P_Tessa_Cards_CardTypeColumn_Flags.htm)|  Флаги, определяющие
дополнительные атрибуты.  
[HeaderAlignment](P_Tessa_Cards_CardTypeColumn_HeaderAlignment.htm)|
Выравнивание заголовка колонки.  
[IsSealed](P_Tessa_Cards_CardSerializableObject_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[MaxLength](P_Tessa_Cards_CardTypeColumn_MaxLength.htm)|  Максимальная
отображаемая длина колонки в ячейке таблицы. Равна null или нулю, если
ограничения отсутствуют.  
[Order](P_Tessa_Cards_CardTypeContent_Order.htm)|  Порядок отображения объекта
в интерфейсе карточки.  
(Унаследован от [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm))  
[OwnedComplexColumnID](P_Tessa_Cards_CardTypeColumn_OwnedComplexColumnID.htm)|
Идентификатор комплексной колонки в дочерней секции или null, если текущий
объект не связан с дочерней секцией или связан только с её физическими
колонками.  
[OwnedOrderColumnID](P_Tessa_Cards_CardTypeColumn_OwnedOrderColumnID.htm)|
Идентификатор колонки в дочерней секции, задающей порядок отображения дочерних
строк, или null, если текущий объект не связан с дочерней секцией или дочерняя
секция не упорядочена.  
[OwnedPhysicalColumnIDList](P_Tessa_Cards_CardTypeColumn_OwnedPhysicalColumnIDList.htm)|
Список идентификаторов физических колонок, которые определяют значения полей
колонки в дочерней секции. Колонки указываются для секции
[OwnedSectionID](P_Tessa_Cards_CardTypeColumn_OwnedSectionID.htm).  
[OwnedSectionID](P_Tessa_Cards_CardTypeColumn_OwnedSectionID.htm)|
Идентификатор дочерней секции или null, если текущий объект не связан с
дочерней секцией.  
[PhysicalColumnIDList](P_Tessa_Cards_CardTypeColumn_PhysicalColumnIDList.htm)|
Список идентификаторов физических колонок, которые определяют значения полей
колонки.  
[Reference](P_Tessa_Cards_CardSerializableObject_Reference.htm)|  Имя
глобального объекта, на который ссылается данный объект.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SelectableControlName](P_Tessa_Cards_CardTypeColumn_SelectableControlName.htm)|
Имя (алиас) контрола, который будет автоматически выбран при открытии строки
по двойному клику по ячейке в этой колонке, или null, если выделяемых
контролов нет.  
[Separator](P_Tessa_Cards_CardTypeColumn_Separator.htm)|  Разделитель между
дочерними строками.  
[ToolTipLineLength](P_Tessa_Cards_CardTypeColumn_ToolTipLineLength.htm)|
Предпочитаемая ширина всплывающей подсказки в символах. Если ширина превышает
это значение, то подсказка разбивается на несколько строк, где строки
переносятся по словам, которые разделены символами категории whitespace в
Unicode. По умолчанию значение равно
[DefaultToolTipLineLength](F_Tessa_Cards_CardTypeColumn_DefaultToolTipLineLength.htm).
Если значение равно 0, то используется
[DefaultToolTipLineLength](F_Tessa_Cards_CardTypeColumn_DefaultToolTipLineLength.htm).
Не должно быть отрицательным числом.  
[XmlElementNameInternal](P_Tessa_Cards_CardTypeColumn_XmlElementNameInternal.htm)|
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
[DeserializeAttributeFromXml](M_Tessa_Cards_CardTypeColumn_DeserializeAttributeFromXml.htm)|
Выполняется для каждого атрибута десериализуемого атрибута.  
(Переопределяет [CardTypeContent.DeserializeAttributeFromXml(String,
String)](M_Tessa_Cards_CardTypeContent_DeserializeAttributeFromXml.htm))  
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
[DeserializeFromBinaryInternal](M_Tessa_Cards_CardTypeColumn_DeserializeFromBinaryInternal.htm)|
Выполняет десериализацию всех полей текущего объекта из байтового потока.  
(Переопределяет
[CardTypeContent.DeserializeFromBinaryInternal(BinaryReader)](M_Tessa_Cards_CardTypeContent_DeserializeFromBinaryInternal.htm))  
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
[DeserializeFromStorageInternal](M_Tessa_Cards_CardTypeColumn_DeserializeFromStorageInternal.htm)|
Выполняет десериализацию объекта и всех его дочерних объектов из хранилища
Dictionary<string, object>.  
(Переопределяет
[CardTypeContent.DeserializeFromStorageInternal(Dictionary<String,
Object>)](M_Tessa_Cards_CardTypeContent_DeserializeFromStorageInternal.htm))  
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
[EqualsInternal](M_Tessa_Cards_CardTypeColumn_EqualsInternal.htm)| Сравнивает
заданный объект с текущим по всем полям.  
(Переопределяет
[CardTypeContent.EqualsInternal(CardTypeContent)](M_Tessa_Cards_CardTypeContent_EqualsInternal.htm))  
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
[OnDeserializing](M_Tessa_Cards_CardTypeColumn_OnDeserializing.htm)|
Выполняется перед десериализацией объекта и всех его дочерних объектов из
элемента XML.  
(Переопределяет
[CardTypeContent.OnDeserializing(SerializationMode)](M_Tessa_Cards_CardTypeContent_OnDeserializing.htm))  
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
[RepairInternalAsync](M_Tessa_Cards_CardSchemeSerializableObject_RepairInternalAsync.htm)|
Метод восстанавливает объект к работоспособному состоянии в соответствии со
схемой. Этот процесс включает удаление данных из текущего объекта, которые
имеют отношение к схеме, но фактически в ней отсутствуют.  
(Унаследован от
[CardSchemeSerializableObject](T_Tessa_Cards_CardSchemeSerializableObject.htm))  
[Seal](M_Tessa_Cards_CardSerializableObject_Seal.htm)| Защищает объект от
изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SealInternal](M_Tessa_Cards_CardTypeColumn_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Переопределяет
[CardSerializableObject.SealInternal()](M_Tessa_Cards_CardSerializableObject_SealInternal.htm))  
[SerializeAttributesToXml](M_Tessa_Cards_CardTypeColumn_SerializeAttributesToXml.htm)|
Выполняет сериализацию текущего объекта в атрибуты XML.  
(Переопределяет
[CardTypeContent.SerializeAttributesToXml(XmlWriter)](M_Tessa_Cards_CardTypeContent_SerializeAttributesToXml.htm))  
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
[SerializeToBinaryInternal](M_Tessa_Cards_CardTypeColumn_SerializeToBinaryInternal.htm)|
Выполняет сериализацию текущего объекта в байтовый поток.  
(Переопределяет
[CardTypeContent.SerializeToBinaryInternal(BinaryWriter)](M_Tessa_Cards_CardTypeContent_SerializeToBinaryInternal.htm))  
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
[SerializeToStorageInternal](M_Tessa_Cards_CardTypeColumn_SerializeToStorageInternal.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в
хранилище Dictionary<string, object>.  
(Переопределяет [CardTypeContent.SerializeToStorageInternal(Dictionary<String,
Object>)](M_Tessa_Cards_CardTypeContent_SerializeToStorageInternal.htm))  
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
[ValidateInternal](M_Tessa_Cards_CardTypeColumn_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Переопределяет
[CardTypeContent.ValidateInternal(IValidationResultBuilder)](M_Tessa_Cards_CardTypeContent_ValidateInternal.htm))  
##  __Поля
[DefaultToolTipLineLength](F_Tessa_Cards_CardTypeColumn_DefaultToolTipLineLength.htm)|
Значение по умолчанию для предпочитаемой ширины всплывающей подсказки в
символах. Если ширина превышает это значение, то подсказка разбивается на
несколько строк, где строки переносятся по словам, которые разделены символами
категории whitespace в Unicode.  
---|---  
[XmlElementName](F_Tessa_Cards_CardTypeColumn_XmlElementName.htm)|  Имя XML-
элемента.  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
