# CardValidationManager - класс
Объект, управляющий валидацией карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardValidationManager : ICardValidationManager
VB __Копировать
     Public NotInheritable Class CardValidationManager
    	Implements ICardValidationManager
C++ __Копировать
     public ref class CardValidationManager sealed : ICardValidationManager
F# __Копировать
     [<SealedAttribute>]
    type CardValidationManager = 
        class
            interface ICardValidationManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardValidationManager
Implements
    [ICardValidationManager](T_Tessa_Cards_Validation_ICardValidationManager.htm)
##  __Конструкторы
[CardValidationManager](M_Tessa_Cards_Validation_CardValidationManager__ctor.htm)|
Создаёт экземпляр класса с указанием используемого реестра экземпляров
валидаторов.  
---|---  
## __Свойства
[Result](P_Tessa_Cards_Validation_CardValidationManager_Result.htm)|
Результат последней валидации.  
---|---  
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
[ValidateCardAsync](M_Tessa_Cards_Validation_CardValidationManager_ValidateCardAsync.htm)|
Выполняет валидацию основной карточки для заданного списка валидаторов.  
[ValidateTaskAsync](M_Tessa_Cards_Validation_CardValidationManager_ValidateTaskAsync.htm)|
Выполняет валидацию основной карточки и её карточки задания для заданного
списка валидаторов.  
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
