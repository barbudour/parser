# DelegateContextPolicy<TContext> \- конструктор
Создаёт экземпляр класса с указанием делегата, проверяющего то, что контекст
удовлетворяет политике.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public DelegateContextPolicy(
    	Func<TContext, bool> isAllowedFunc
    )
VB __Копировать
     Public Sub New ( 
    	isAllowedFunc As Func(Of TContext, Boolean)
    )
C++ __Копировать
     public:
    DelegateContextPolicy(
    	Func<TContext, bool>^ isAllowedFunc
    )
F# __Копировать
     new : 
            isAllowedFunc : Func<'TContext, bool> -> DelegateContextPolicy
#### Параметры
isAllowedFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[TContext](T_Tessa_Extensions_DelegateContextPolicy_1.htm),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
     Функция, получающая контекст (не равный null) и возвращающая признак того, что контекст удовлетворяет политике. Параметр не равен null. Исключения логируются в логгере [Extensions](F_Tessa_Platform_TessaLoggers_Extensions.htm), а также добавляются в контекст как сообщение валидации, если он реализует интерфейс [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm). Расширение, для которого возникло исключение, пропускается. 
## __См. также
#### Ссылки
[DelegateContextPolicy<TContext> \-
](T_Tessa_Extensions_DelegateContextPolicy_1.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
