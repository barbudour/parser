# ConditionsCardRepairExtensionBase - класс
Базовый класс расширения на починку условий при импорте карточек с помощью
[IConditionRepairManager](T_Tessa_Platform_Conditions_IConditionRepairManager.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Shared.Conditions](N_Tessa_Extensions_Platform_Shared_Conditions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ConditionsCardRepairExtensionBase : CardRepairExtension
VB __Копировать
     Public MustInherit Class ConditionsCardRepairExtensionBase
    	Inherits CardRepairExtension
C++ __Копировать
     public ref class ConditionsCardRepairExtensionBase abstract : public CardRepairExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type ConditionsCardRepairExtensionBase = 
        class
            inherit CardRepairExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardRepairExtension](T_Tessa_Cards_Extensions_CardRepairExtension.htm) __ ConditionsCardRepairExtensionBase
Derived
[Tessa.Extensions.Default.Shared.Conditions.DefaultConditionsCardRepairExtension](T_Tessa_Extensions_Default_Shared_Conditions_DefaultConditionsCardRepairExtension.htm)
[Tessa.Extensions.Platform.Shared.Conditions.PlatformConditionsCardRepairExtension](T_Tessa_Extensions_Platform_Shared_Conditions_PlatformConditionsCardRepairExtension.htm)
##  __Конструкторы
[ConditionsCardRepairExtensionBase](M_Tessa_Extensions_Platform_Shared_Conditions_ConditionsCardRepairExtensionBase__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[AfterRequest](M_Tessa_Extensions_Platform_Shared_Conditions_ConditionsCardRepairExtensionBase_AfterRequest.htm)|
Действие, выполняемое после исправления структуры карточки как при успешном,
так и при неудачном результате.  
(Переопределяет
[CardRepairExtension.AfterRequest(ICardRepairExtensionContext)](M_Tessa_Cards_Extensions_CardRepairExtension_AfterRequest.htm))  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardRepairExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после исправления
структуры карточки как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardRepairExtension](T_Tessa_Cards_Extensions_CardRepairExtension.htm))  
[BeforeRequest](M_Tessa_Cards_Extensions_CardRepairExtension_BeforeRequest.htm)|
Действие, выполняемое перед исправлением структуры карточки.  
(Унаследован от
[CardRepairExtension](T_Tessa_Cards_Extensions_CardRepairExtension.htm))  
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
[Tessa.Extensions.Platform.Shared.Conditions - пространство
имён](N_Tessa_Extensions_Platform_Shared_Conditions.htm)
