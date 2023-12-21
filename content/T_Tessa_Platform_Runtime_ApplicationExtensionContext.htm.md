# ApplicationExtensionContext - класс
Контекст расширений, связанных с жизненным циклом приложения.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ApplicationExtensionContext : ApplicationExtensionContextBase, 
    	IApplicationExtensionContext, IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
VB __Копировать
     Public Class ApplicationExtensionContext
    	Inherits ApplicationExtensionContextBase
    	Implements IApplicationExtensionContext, IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
C++ __Копировать
     public ref class ApplicationExtensionContext : public ApplicationExtensionContextBase, 
    	IApplicationExtensionContext, IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
F# __Копировать
     type ApplicationExtensionContext = 
        class
            inherit ApplicationExtensionContextBase
            interface IApplicationExtensionContext
            interface IApplicationExtensionContextBase
            interface ITraceableExtensionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm) __ ApplicationExtensionContext
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm), [IApplicationExtensionContext](T_Tessa_Platform_Runtime_IApplicationExtensionContext.htm), [IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm)
##  __Заметки
Наследники класса могут добавлять дополнительные свойства и реализовывать
интерфейсы.
## __Конструкторы
[ApplicationExtensionContext](M_Tessa_Platform_Runtime_ApplicationExtensionContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[ApplicationClosingAfterCheck](P_Tessa_Platform_Runtime_ApplicationExtensionContext_ApplicationClosingAfterCheck.htm)|
Событие по закрытию окна приложения, выполняемое после того, как пользователь
был проинформирован о необходимости сохранить изменения во вкладках и
подтвердил закрытие, несмотря на это. Если обработчики события
[IApplicationExtensionContext.ClosingBeforeCheck] уже отменили закрытие,
установив e.Cancel = true, или обработчики вызвали исключение, то это событие
не будет вызвано, а закрытие будет отменено. Если пользователь подтвердил
закрытие или обработчики события
[IApplicationExtensionContext.ClosingBeforeCheck] установили e.ForceClosing =
true, то это событие будет вызвано, но в этом случае будет установлено
e.Cancel = true в аргументах события. В платформе по умолчанию событие
вызывается только в приложении TessaClient.  
---|---  
[ApplicationClosingBeforeCheck](P_Tessa_Platform_Runtime_ApplicationExtensionContext_ApplicationClosingBeforeCheck.htm)|
Событие по закрытию окна приложения, выполняемое до того, как будут сделаны
проверки по умолчанию, и пользователь будет проинформирован о необходимости
сохранить изменения во вкладках. В платформе по умолчанию событие вызывается
только в приложении TessaClient.  
[ApplicationID](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_ApplicationID.htm)|
Идентификатор приложения, для которого выполняются расширения. Стандартные
идентификаторы приложений указаны в полях класса
[Tessa.Platform.Runtime.ApplicationIdentifiers].  
(Унаследован от
[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm))  
[CancellationToken](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от
[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm))  
[EnableTracing](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
(Унаследован от
[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm))  
[Info](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_Info.htm)|
Дополнительная информация, связанная с контекстом расширений.  
(Унаследован от
[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm))  
[Session](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_Session.htm)|
Сессия текущего пользователя.  
(Унаследован от
[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm))  
[ValidationResult](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
(Унаследован от
[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm))  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
