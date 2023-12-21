# AdvancedRoleManager - класс
Объект, выполняющий задания, связанные с пересчётом ролей и замещений.
Доступен на сервере.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class AdvancedRoleManager : RoleManager
VB __Копировать
     Public Class AdvancedRoleManager
    	Inherits RoleManager
C++ __Копировать
     public ref class AdvancedRoleManager : public RoleManager
F# __Копировать
     type AdvancedRoleManager = 
        class
            inherit RoleManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[RoleManager](T_Tessa_Roles_RoleManager.htm) __ AdvancedRoleManager
##  __Заметки
Наследники класса могут переопределить его методы.
## __Конструкторы
[AdvancedRoleManager](M_Tessa_Roles_AdvancedRoleManager__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[RoleTimeoutSeconds](P_Tessa_Roles_RoleManager_RoleTimeoutSeconds.htm)|
Таймаут выполнения длительных запросов с ролями.  
(Унаследован от [RoleManager](T_Tessa_Roles_RoleManager.htm))  
---|---  
##  __Методы
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
[RecalcDynamicRoleAsync](M_Tessa_Roles_RoleManager_RecalcDynamicRoleAsync.htm)|
Выполняет пересчёт указанной динамической роли.  
(Унаследован от [RoleManager](T_Tessa_Roles_RoleManager.htm))  
[RecalcDynamicRoleCoreAsync](M_Tessa_Roles_RoleManager_RecalcDynamicRoleCoreAsync.htm)|
Выполняет пересчёт указанной динамической роли.  
(Унаследован от [RoleManager](T_Tessa_Roles_RoleManager.htm))  
[RecalcRoleGeneratorAsync](M_Tessa_Roles_RoleManager_RecalcRoleGeneratorAsync.htm)|
Выполняет пересчёт метаролей для указанного генератора.  
(Унаследован от [RoleManager](T_Tessa_Roles_RoleManager.htm))  
[RecalcRoleGeneratorCoreAsync](M_Tessa_Roles_RoleManager_RecalcRoleGeneratorCoreAsync.htm)|
Выполняет пересчёт метаролей для указанного генератора.  
(Унаследован от [RoleManager](T_Tessa_Roles_RoleManager.htm))  
[SyncAllDeputiesAsync](M_Tessa_Roles_RoleManager_SyncAllDeputiesAsync.htm)|
Выполняет пересчёт замещений для всех ролей, кроме динамических ролей и
метаролей.  
(Унаследован от [RoleManager](T_Tessa_Roles_RoleManager.htm))  
[SyncAllDeputiesCoreAsync](M_Tessa_Roles_AdvancedRoleManager_SyncAllDeputiesCoreAsync.htm)|
Выполняет пересчёт замещений для всех ролей, кроме динамических ролей и
метаролей.  
(Переопределяет [RoleManager.SyncAllDeputiesCoreAsync(Int32, Int32,
Func<Boolean>,
CancellationToken)](M_Tessa_Roles_RoleManager_SyncAllDeputiesCoreAsync.htm))  
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
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)
