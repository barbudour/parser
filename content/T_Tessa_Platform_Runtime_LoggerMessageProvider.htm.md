# LoggerMessageProvider - класс
Объект, обеспечивающий вывод сообщений в лог без отображения их пользователю.
Используется, например, для вывода сообщений в
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm). Подтверждение в
методе [ConfirmAsync(String, String,
CancellationToken)](M_Tessa_Platform_Runtime_LoggerMessageProvider_ConfirmAsync.htm),
запрашиваемое у пользователя, всегда возвращает true.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class LoggerMessageProvider : IMessageProvider
VB __Копировать
     Public NotInheritable Class LoggerMessageProvider
    	Implements IMessageProvider
C++ __Копировать
     public ref class LoggerMessageProvider sealed : IMessageProvider
F# __Копировать
     [<SealedAttribute>]
    type LoggerMessageProvider = 
        class
            interface IMessageProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LoggerMessageProvider
Implements
    [IMessageProvider](T_Tessa_Platform_Runtime_IMessageProvider.htm)
##  __Конструкторы
[LoggerMessageProvider()](M_Tessa_Platform_Runtime_LoggerMessageProvider__ctor.htm)|
Создаёт экземпляр класса с использованием способа логирования по умолчанию.  
---|---  
[LoggerMessageProvider(ILogger)](M_Tessa_Platform_Runtime_LoggerMessageProvider__ctor_1.htm)|
Создаёт экземпляр класса с использованием заданного объекта логирования.  
## __Методы
[ConfirmAsync](M_Tessa_Platform_Runtime_LoggerMessageProvider_ConfirmAsync.htm)|
Выводит заданное сообщение и ожидает ответа да/нет. Возвращает признак того,
что пользователь выбрал "да".  
---|---  
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
[ShowExceptionAsync](M_Tessa_Platform_Runtime_LoggerMessageProvider_ShowExceptionAsync.htm)|
Выводит информацию по исключению.  
[ShowNotEmptyAsync](M_Tessa_Platform_Runtime_LoggerMessageProvider_ShowNotEmptyAsync.htm)|
Выводит сообщение с результатом валидации, если он не пустой.  
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
