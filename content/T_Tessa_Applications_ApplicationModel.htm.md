# ApplicationModel - класс
Модель приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApplicationModel : IApplicationModel, 
    	IApplicationMessageObserver, IDisposable, IComparable, IComparable<IApplicationModel>
VB __Копировать
     Public NotInheritable Class ApplicationModel
    	Implements IApplicationModel, IApplicationMessageObserver, IDisposable, IComparable, 
    	IComparable(Of IApplicationModel)
C++ __Копировать
     public ref class ApplicationModel sealed : IApplicationModel, 
    	IApplicationMessageObserver, IDisposable, IComparable, IComparable<IApplicationModel^>
F# __Копировать
     [<SealedAttribute>]
    type ApplicationModel = 
        class
            interface IApplicationModel
            interface IApplicationMessageObserver
            interface IDisposable
            interface IComparable
            interface IComparable<IApplicationModel>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationModel
Implements
    [IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable), [IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable-1)<[IApplicationModel](T_Tessa_Applications_IApplicationModel.htm)>, [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IApplicationModel](T_Tessa_Applications_IApplicationModel.htm), [IApplicationMessageObserver](T_Tessa_Applications_Services_ApplicationManager_IApplicationMessageObserver.htm)
##  __Конструкторы
[ApplicationModel](M_Tessa_Applications_ApplicationModel__ctor.htm)|
Initializes a new instance of the ApplicationModel class.  
---|---  
## __Свойства
[ApplicationCatalog](P_Tessa_Applications_ApplicationModel_ApplicationCatalog.htm)|
Gets Модель каталога приложений которому принадлежит приложение  
---|---  
[ApplicationPackage](P_Tessa_Applications_ApplicationModel_ApplicationPackage.htm)|
Gets Пакет приложения  
[BaseAddress](P_Tessa_Applications_ApplicationModel_BaseAddress.htm)|  Gets
Базовый адрес сервиса приложения  
[IsDefaultInstance](P_Tessa_Applications_ApplicationModel_IsDefaultInstance.htm)|
Gets or sets a value indicating whether Признак экземпляра по умолчанию  
[ServerCode](P_Tessa_Applications_ApplicationModel_ServerCode.htm)|  Gets Имя
экземпляра сервиса  
[SkipWinAuth](P_Tessa_Applications_ApplicationModel_SkipWinAuth.htm)|  Признак
того, что аутентификация Windows не выполняется, если не введён логин и
пароль.  
[State](P_Tessa_Applications_ApplicationModel_State.htm)|  Gets Состояние
приложения  
## __Методы
[AttachMonitor](M_Tessa_Applications_ApplicationModel_AttachMonitor.htm)|
Устанавливает мониторинг установки приложения  
---|---  
[CompareTo(IApplicationModel)](M_Tessa_Applications_ApplicationModel_CompareTo_1.htm)|
Compares the current instance with another object of the same type and returns
an integer that indicates whether the current instance precedes, follows, or
occurs in the same position in the sort order as the other object.  
[CompareTo(Object)](M_Tessa_Applications_ApplicationModel_CompareTo.htm)|
Compares the current instance with another object of the same type and returns
an integer that indicates whether the current instance precedes, follows, or
occurs in the same position in the sort order as the other object.  
[Dispose](M_Tessa_Applications_ApplicationModel_Dispose.htm)| Performs
application-defined tasks associated with freeing, releasing, or resetting
unmanaged resources.  
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
[LaunchAsync](M_Tessa_Applications_ApplicationModel_LaunchAsync.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnMessage](M_Tessa_Applications_ApplicationModel_OnMessage.htm)|  Вызывает
обработку сообщения message  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[ApplicationClosed](E_Tessa_Applications_ApplicationModel_ApplicationClosed.htm)|
Событие закрытия приложения  
---|---  
[ApplicationLaunched](E_Tessa_Applications_ApplicationModel_ApplicationLaunched.htm)|
Событие успешного запуска приложения  
[ApplicationLaunchFailed](E_Tessa_Applications_ApplicationModel_ApplicationLaunchFailed.htm)|
Событие сбоя при запуске приложения  
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
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
