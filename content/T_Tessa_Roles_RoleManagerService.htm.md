# RoleManagerService - класс
Объект, выполняющий задания, связанные с пересчётом ролей и замещений.
Доступен на сервере, а также на клиенте при условии, что на клиенте
зарегистрированы API карточек и платформенные расширения.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class RoleManagerService : IRoleManagerService
VB __Копировать
     Public NotInheritable Class RoleManagerService
    	Implements IRoleManagerService
C++ __Копировать
     public ref class RoleManagerService sealed : IRoleManagerService
F# __Копировать
     [<SealedAttribute>]
    type RoleManagerService = 
        class
            interface IRoleManagerService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RoleManagerService
Implements
    [IRoleManagerService](T_Tessa_Roles_IRoleManagerService.htm)
##  __Конструкторы
[RoleManagerService](M_Tessa_Roles_RoleManagerService__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
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
[RecalcAllDynamicRolesAsync](M_Tessa_Roles_RoleManagerService_RecalcAllDynamicRolesAsync.htm)|
Выполняет пересчёт всех динамических ролей. Возвращает результат операции.  
[RecalcAllRoleGeneratorsAsync](M_Tessa_Roles_RoleManagerService_RecalcAllRoleGeneratorsAsync.htm)|
Выполняет пересчёт всех генераторов метаролей. Возвращает результат операции.  
[RecalcDynamicRoleAsync](M_Tessa_Roles_RoleManagerService_RecalcDynamicRoleAsync.htm)|
Выполняет пересчёт указанной динамической роли. Возвращает результат операции.  
[RecalcRoleGeneratorAsync](M_Tessa_Roles_RoleManagerService_RecalcRoleGeneratorAsync.htm)|
Выполняет пересчёт метаролей для указанного генератора. Возвращает результат
операции.  
[SyncAllDeputiesAsync](M_Tessa_Roles_RoleManagerService_SyncAllDeputiesAsync.htm)|
Выполняет пересчёт замещений для всех ролей, кроме динамических ролей и
метаролей. Возвращает результат операции.  
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
