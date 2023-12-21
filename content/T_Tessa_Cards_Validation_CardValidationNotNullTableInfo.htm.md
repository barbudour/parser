# CardValidationNotNullTableInfo - класс
Информация по секции, для которой требуется выполнить валидацию для валидатора
[NotNullTable](F_Tessa_Cards_CardValidatorTypes_NotNullTable.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardValidationNotNullTableInfo
VB __Копировать
     Public NotInheritable Class CardValidationNotNullTableInfo
C++ __Копировать
     public ref class CardValidationNotNullTableInfo sealed
F# __Копировать
     [<SealedAttribute>]
    type CardValidationNotNullTableInfo = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardValidationNotNullTableInfo
##  __Конструкторы
[CardValidationNotNullTableInfo](M_Tessa_Cards_Validation_CardValidationNotNullTableInfo__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[CardType](P_Tessa_Cards_Validation_CardValidationNotNullTableInfo_CardType.htm)|
Тип карточки, файла или задания, к которому принадлежит секция.  
---|---  
[Instance](P_Tessa_Cards_Validation_CardValidationNotNullTableInfo_Instance.htm)|
Проверяемый объект, по которому могут быть получены секции и идентификатор.
Может быть объектом карточки, файла или задания.  
[Section](P_Tessa_Cards_Validation_CardValidationNotNullTableInfo_Section.htm)|
Секция, в которой требуется проверить наличие строк.  
[StoreMode](P_Tessa_Cards_Validation_CardValidationNotNullTableInfo_StoreMode.htm)|
Режим сохранения карточки. Поскольку
[Instance](P_Tessa_Cards_Validation_CardValidationNotNullTableInfo_Instance.htm)
может быть заданием, то режим сохранения определяем отдельным свойством.  
[Validator](P_Tessa_Cards_Validation_CardValidationNotNullTableInfo_Validator.htm)|
Валидатор, инициировавший проверку.  
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
