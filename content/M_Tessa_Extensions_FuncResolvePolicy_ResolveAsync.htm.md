# FuncResolvePolicy.ResolveAsync - метод
Получает экземпляр расширения для ключа типа расширения и типа экземпляра
расширения.
##  __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IExtension> ResolveAsync(
    	ExtensionBuildKey buildKey,
    	ExtensionResolveKey resolveKey,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ResolveAsync ( 
    	buildKey As ExtensionBuildKey,
    	resolveKey As ExtensionResolveKey,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IExtension)
C++ __Копировать
     public:
    virtual ValueTask<IExtension^> ResolveAsync(
    	ExtensionBuildKey^ buildKey, 
    	ExtensionResolveKey^ resolveKey, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ResolveAsync : 
            buildKey : ExtensionBuildKey * 
            resolveKey : ExtensionResolveKey * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IExtension> 
    override ResolveAsync : 
            buildKey : ExtensionBuildKey * 
            resolveKey : ExtensionResolveKey * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IExtension> 
#### Параметры
buildKey [ExtensionBuildKey](T_Tessa_Extensions_ExtensionBuildKey.htm)
    Ключ, используемый для идентификации типа расширения.
resolveKey [ExtensionResolveKey](T_Tessa_Extensions_ExtensionResolveKey.htm)
    Ключ, используемый для идентификации экземпляра расширения.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IExtension](T_Tessa_Extensions_IExtension.htm)>  
Экземпляр расширения. Должен реализовывать тип, указанный в ключе resolveKey.
#### Реализации
[IResolvePolicy.ResolveAsync(ExtensionBuildKey, ExtensionResolveKey,
CancellationToken)](M_Tessa_Extensions_IResolvePolicy_ResolveAsync.htm)  
##  __См. также
#### Ссылки
[FuncResolvePolicy - ](T_Tessa_Extensions_FuncResolvePolicy.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
