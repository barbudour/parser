# DefaultDelegateContextPolicy - конструктор
Инициализирует новый экземпляр класса
[DefaultDelegateContextPolicy](T_Tessa_Extensions_DefaultDelegateContextPolicy.htm)
##  __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public DefaultDelegateContextPolicy(
    	Func<IExtensionContext, bool> isAllowedFunc
    )
VB __Копировать
     Public Sub New ( 
    	isAllowedFunc As Func(Of IExtensionContext, Boolean)
    )
C++ __Копировать
     public:
    DefaultDelegateContextPolicy(
    	Func<IExtensionContext^, bool>^ isAllowedFunc
    )
F# __Копировать
     new : 
            isAllowedFunc : Func<IExtensionContext, bool> -> DefaultDelegateContextPolicy
#### Параметры
isAllowedFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
## __См. также
#### Ссылки
[DefaultDelegateContextPolicy -
](T_Tessa_Extensions_DefaultDelegateContextPolicy.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
