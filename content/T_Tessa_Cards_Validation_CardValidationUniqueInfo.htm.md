# CardValidationUniqueInfo - класс
Информация по секции и колонке, для которой требуется выполнить валидацию для
валидатора [Unique](F_Tessa_Cards_CardValidatorTypes_Unique.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardValidationUniqueInfo
VB __Копировать
     Public NotInheritable Class CardValidationUniqueInfo
C++ __Копировать
     public ref class CardValidationUniqueInfo sealed
F# __Копировать
     [<SealedAttribute>]
    type CardValidationUniqueInfo = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardValidationUniqueInfo
##  __Конструкторы
[CardValidationUniqueInfo](M_Tessa_Cards_Validation_CardValidationUniqueInfo__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[CardType](P_Tessa_Cards_Validation_CardValidationUniqueInfo_CardType.htm)|
Тип карточки, файла или задания, к которому принадлежит секция.  
---|---  
[Instance](P_Tessa_Cards_Validation_CardValidationUniqueInfo_Instance.htm)|
Проверяемый объект, по которому могут быть получены секции и идентификатор.
Может быть объектом карточки, файла или задания.  
[MainColumn](P_Tessa_Cards_Validation_CardValidationUniqueInfo_MainColumn.htm)|
Колонка в родительской секции или null, если родительская секция не задана.  
[OrderColumn](P_Tessa_Cards_Validation_CardValidationUniqueInfo_OrderColumn.htm)|
Физическая колонка для сортировки в секции
[Section](P_Tessa_Cards_Validation_CardValidationUniqueInfo_Section.htm) или
null, если колонка для сортировки не задана.  
[ParentMainColumn](P_Tessa_Cards_Validation_CardValidationUniqueInfo_ParentMainColumn.htm)|
Комплексная или физическая колонка, в которой требуется проверить уникальность
значения.  
[ParentPhysicalColumns](P_Tessa_Cards_Validation_CardValidationUniqueInfo_ParentPhysicalColumns.htm)|
Физические колонки в родительской секции или пустая коллекция, если
родительская секция не задана. Если валидатор был связан с комплексной
колонкой, то свойство содержит все ключевые колонки внутри комплексной. В
противном случае свойство содержит единственную физическую колонку, с которой
был связан валидатор.  
[ParentSection](P_Tessa_Cards_Validation_CardValidationUniqueInfo_ParentSection.htm)|
Родительская секция или null, если родительская секция не задана.  
[PhysicalColumns](P_Tessa_Cards_Validation_CardValidationUniqueInfo_PhysicalColumns.htm)|
Физические колонки, в которых требуется проверить уникальность значения. Если
валидатор был связан с комплексной колонкой, то свойство содержит все ключевые
колонки внутри комплексной. В противном случае свойство содержит единственную
физическую колонку, с которой был связан валидатор.  
[RemoveDuplicates](P_Tessa_Cards_Validation_CardValidationUniqueInfo_RemoveDuplicates.htm)|
Признак того, что дубликаты, найденные в коллекционной секции, должны быть
автоматически удалены.  
[Section](P_Tessa_Cards_Validation_CardValidationUniqueInfo_Section.htm)|
Секция, в которой требуется проверить уникальность значения.  
[StoreMode](P_Tessa_Cards_Validation_CardValidationUniqueInfo_StoreMode.htm)|
Режим сохранения карточки. Поскольку
[Instance](P_Tessa_Cards_Validation_CardValidationUniqueInfo_Instance.htm)
может быть заданием, то режим сохранения определяем отдельным свойством.  
[ValidationMode](P_Tessa_Cards_Validation_CardValidationUniqueInfo_ValidationMode.htm)|
Способ выполнения валидации.  
[Validator](P_Tessa_Cards_Validation_CardValidationUniqueInfo_Validator.htm)|
Валидатор, инициировавший проверку секции.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
