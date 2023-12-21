# DelegateContextPolicy<TContext>.IsAllowedFunc - свойство
Функция, получающая контекст (не равный null) и возвращающая признак того, что
контекст удовлетворяет политике. Значение не равно null.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected Func<TContext, bool> IsAllowedFunc { get; }
VB __Копировать
     Protected ReadOnly Property IsAllowedFunc As Func(Of TContext, Boolean)
    	Get
C++ __Копировать
     protected:
    property Func<TContext, bool>^ IsAllowedFunc {
    	Func<TContext, bool>^ get ();
    }
F# __Копировать
     member IsAllowedFunc : Func<'TContext, bool> with get
#### Значение свойства
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[TContext](T_Tessa_Extensions_DelegateContextPolicy_1.htm),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
##  __См. также
#### Ссылки
[DelegateContextPolicy<TContext> \-
](T_Tessa_Extensions_DelegateContextPolicy_1.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
