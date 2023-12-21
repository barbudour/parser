# ErrorManager - класс
Объект, управляющий отправкой и получением ошибок. Получение информации по
ошибкам обычно доступно только на сервере.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ErrorManager : IErrorManager
VB __Копировать
     Public NotInheritable Class ErrorManager
    	Implements IErrorManager
C++ __Копировать
     public ref class ErrorManager sealed : IErrorManager
F# __Копировать
     [<SealedAttribute>]
    type ErrorManager = 
        class
            interface IErrorManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ErrorManager
Implements
    [IErrorManager](T_Tessa_Platform_Runtime_IErrorManager.htm)
##  __Конструкторы
[ErrorManager(IErrorDescriptionSerializer, ISession, ISequentialGuidProvider,
IActionHistoryStrategy, ITypeInfoResolver,
IErrorDetailWriter)](M_Tessa_Platform_Runtime_ErrorManager__ctor_1.htm)|
Создаёт экземпляр класса с указанием его зависимостей на клиенте.  
---|---  
[ErrorManager(IErrorDescriptionSerializer, ISession, IDbScope,
ISequentialGuidProvider, IActionHistoryStrategy, ITypeInfoResolver,
IErrorDetailWriter)](M_Tessa_Platform_Runtime_ErrorManager__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей на сервере.  
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
[ReportErrorAsync](M_Tessa_Platform_Runtime_ErrorManager_ReportErrorAsync.htm)|
Сообщает об ошибке с заданными параметрами и с необязательным дополнительным
описанием, в т.ч. с файлами. Для ошибки создаётся карточка с детальным
описанием и с заданным идентификатором, в которой можно выполнять поиск по
категории и тексту. Метод возвращает идентификатор фактически созданной
ошибки. Если при отправке ошибки возникло исключение, то оно будет выброшено
наружу. Используйте метод ReportErrorSafe (using Tessa.Platform.Runtime),
чтобы поглощать исключения, возникшие при отправке.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetAsync](M_Tessa_Platform_Runtime_ErrorManager_TryGetAsync.htm)|
Возвращает описание ошибки Description и запись в истории действий Record, или
null, если ошибка не найдена по заданному идентификатору. Обычно метод
доступен только на сервере, на клиенте он будет возвращать null.  
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
[ReportErrorSafeAsync](M_Tessa_Platform_Runtime_RuntimeExtensions_ReportErrorSafeAsync.htm)|
Сообщает об ошибке с заданными параметрами и с необязательным дополнительным
описанием, в т.ч. с файлами. Для ошибки создаётся карточка с детальным
описанием и с заданным идентификатором, в которой можно выполнять поиск по
категории и тексту. Если при отправке ошибки возникло любое исключение, то оно
поглощается и заносится в лог [Error](F_Tessa_Platform_TessaLoggers_Error.htm)
Метод возвращает идентификатор фактически созданной ошибки или null, если при
отправке ошибки возникло исключение.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
