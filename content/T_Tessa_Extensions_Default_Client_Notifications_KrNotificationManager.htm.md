# KrNotificationManager - класс
Объект, управляющий уведомлениями по новым заданиям.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Notifications](N_Tessa_Extensions_Default_Client_Notifications.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public class KrNotificationManager : IKrNotificationManager, 
    	IDisposable
VB __Копировать
     Public Class KrNotificationManager
    	Implements IKrNotificationManager, IDisposable
C++ __Копировать
     public ref class KrNotificationManager : IKrNotificationManager, 
    	IDisposable
F# __Копировать
     type KrNotificationManager = 
        class
            interface IKrNotificationManager
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrNotificationManager
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IKrNotificationManager](T_Tessa_Extensions_Default_Client_Notifications_IKrNotificationManager.htm)
##  __Конструкторы
[KrNotificationManager](M_Tessa_Extensions_Default_Client_Notifications_KrNotificationManager__ctor.htm)|
Инициализирует новый экземпляр класса KrNotificationManager  
---|---  
##  __Свойства
[IsDisposed](P_Tessa_Extensions_Default_Client_Notifications_KrNotificationManager_IsDisposed.htm)|  
---|---  
## __Методы
[CanCheckTasksAsync](M_Tessa_Extensions_Default_Client_Notifications_KrNotificationManager_CanCheckTasksAsync.htm)|
Возвращает признак того, что уведомления по заданиям включены.  
---|---  
[CheckTasksAsync](M_Tessa_Extensions_Default_Client_Notifications_KrNotificationManager_CheckTasksAsync.htm)|
Проверяет новые задания и отображает уведомления, если они есть. Метод
вызывается в потоке UI, но фактическое отображение должно быть асинхронное.  
[CheckTasksCoreAsync](M_Tessa_Extensions_Default_Client_Notifications_KrNotificationManager_CheckTasksCoreAsync.htm)|  
[Dispose()](M_Tessa_Extensions_Default_Client_Notifications_KrNotificationManager_Dispose.htm)|
Освобождает все ресурсы, используемые объектом KrNotificationManager  
[Dispose(Boolean)](M_Tessa_Extensions_Default_Client_Notifications_KrNotificationManager_Dispose_1.htm)|
Освобождает неуправляемые ресурсы, используемые объектом
KrNotificationManager, а при необходимости освобождает также управляемые
ресурсы  
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
[InitializeAsync](M_Tessa_Extensions_Default_Client_Notifications_KrNotificationManager_InitializeAsync.htm)|
Подготавливаем инфраструктуру для периодического затягивания информации по
новым заданиям. При этом сам запрос [CheckTasksAsync(Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Client_Notifications_KrNotificationManager_CheckTasksAsync.htm)
выполнять не требуется.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ShutdownAsync](M_Tessa_Extensions_Default_Client_Notifications_KrNotificationManager_ShutdownAsync.htm)|
Освобождает инфраструктуру для периодического затягивания информации по новым
заданиям.  
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
[Tessa.Extensions.Default.Client.Notifications - пространство
имён](N_Tessa_Extensions_Default_Client_Notifications.htm)
