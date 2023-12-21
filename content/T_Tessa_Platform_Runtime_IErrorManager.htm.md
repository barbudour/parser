# IErrorManager - интерфейс
Объект, управляющий отправкой и получением ошибок.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IErrorManager
VB __Копировать
     Public Interface IErrorManager
C++ __Копировать
     public interface class IErrorManager
F# __Копировать
     type IErrorManager = interface end
##  __Методы
[ReportErrorAsync](M_Tessa_Platform_Runtime_IErrorManager_ReportErrorAsync.htm)|
Сообщает об ошибке с заданными параметрами и с необязательным дополнительным
описанием, в т.ч. с файлами. Для ошибки создаётся карточка с детальным
описанием и с заданным идентификатором, в которой можно выполнять поиск по
категории и тексту. Метод возвращает идентификатор фактически созданной
ошибки. Если при отправке ошибки возникло исключение, то оно будет выброшено
наружу. Используйте метод ReportErrorSafe (using Tessa.Platform.Runtime),
чтобы поглощать исключения, возникшие при отправке.  
---|---  
[TryGetAsync](M_Tessa_Platform_Runtime_IErrorManager_TryGetAsync.htm)|
Возвращает описание ошибки Description и запись в истории действий Record, или
null, если ошибка не найдена по заданному идентификатору. Обычно метод
доступен только на сервере, на клиенте он будет возвращать null.  
## __Методы расширения
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
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
