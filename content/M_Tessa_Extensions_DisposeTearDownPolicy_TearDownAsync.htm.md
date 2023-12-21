# DisposeTearDownPolicy.TearDownAsync - метод
Освобождает ресурсы, занятые заданным экземпляром расширений.
##  __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask TearDownAsync(
    	ExtensionBuildKey buildKey,
    	Object extension,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TearDownAsync ( 
    	buildKey As ExtensionBuildKey,
    	extension As Object,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask TearDownAsync(
    	ExtensionBuildKey^ buildKey, 
    	Object^ extension, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TearDownAsync : 
            buildKey : ExtensionBuildKey * 
            extension : Object * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override TearDownAsync : 
            buildKey : ExtensionBuildKey * 
            extension : Object * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
buildKey [ExtensionBuildKey](T_Tessa_Extensions_ExtensionBuildKey.htm)
    Ключ, используемый для идентификации типа расширения.
extension [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Экземпляр расширения, ресурсы которого требуется освободить.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
#### Реализации
[ITearDownPolicy.TearDownAsync(ExtensionBuildKey, Object,
CancellationToken)](M_Tessa_Extensions_ITearDownPolicy_TearDownAsync.htm)  
##  __См. также
#### Ссылки
[DisposeTearDownPolicy - ](T_Tessa_Extensions_DisposeTearDownPolicy.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
