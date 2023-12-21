# FuncResolvePolicy - конструктор
Создаёт экземпляр класса с указанием функции, используемой для получения
экземпляра расширения.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FuncResolvePolicy(
    	Func<ExtensionBuildKey, ExtensionResolveKey, CancellationToken, ValueTask<IExtension>> resolveFuncAsync
    )
VB __Копировать
     Public Sub New ( 
    	resolveFuncAsync As Func(Of ExtensionBuildKey, ExtensionResolveKey, CancellationToken, ValueTask(Of IExtension))
    )
C++ __Копировать
     public:
    FuncResolvePolicy(
    	Func<ExtensionBuildKey^, ExtensionResolveKey^, CancellationToken, ValueTask<IExtension^>>^ resolveFuncAsync
    )
F# __Копировать
     new : 
            resolveFuncAsync : Func<ExtensionBuildKey, ExtensionResolveKey, CancellationToken, ValueTask<IExtension>> -> FuncResolvePolicy
#### Параметры
resolveFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-4)<[ExtensionBuildKey](T_Tessa_Extensions_ExtensionBuildKey.htm),
[ExtensionResolveKey](T_Tessa_Extensions_ExtensionResolveKey.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IExtension](T_Tessa_Extensions_IExtension.htm)>>
    Функция, используемая для получения экземпляра расширения.
##  __См. также
#### Ссылки
[FuncResolvePolicy - ](T_Tessa_Extensions_FuncResolvePolicy.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
