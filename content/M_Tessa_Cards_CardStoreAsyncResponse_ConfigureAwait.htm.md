# CardStoreAsyncResponse.ConfigureAwait - метод
Настраивает ожидание задачи.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ConfiguredTaskAwaitable<CardStoreResponse> ConfigureAwait(
    	bool continueOnCapturedContext
    )
VB __Копировать
     Public Function ConfigureAwait ( 
    	continueOnCapturedContext As Boolean
    ) As ConfiguredTaskAwaitable(Of CardStoreResponse)
C++ __Копировать
     public:
    virtual ConfiguredTaskAwaitable<CardStoreResponse^> ConfigureAwait(
    	bool continueOnCapturedContext
    ) sealed
F# __Копировать
     abstract ConfigureAwait : 
            continueOnCapturedContext : bool -> ConfiguredTaskAwaitable<CardStoreResponse> 
    override ConfigureAwait : 
            continueOnCapturedContext : bool -> ConfiguredTaskAwaitable<CardStoreResponse> 
#### Параметры
continueOnCapturedContext
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что выполнение продолжается после ожидания на исходном SynchronizationContext. 
#### Возвращаемое значение
[ConfiguredTaskAwaitable](https://learn.microsoft.com/dotnet/api/system.runtime.compilerservices.configuredtaskawaitable-1)<[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)>  
Объект, определяющий настраиваемое ожидание задачи.
#### Реализации
[ICardStoreAsyncResponse.ConfigureAwait(Boolean)](M_Tessa_Cards_ICardStoreAsyncResponse_ConfigureAwait.htm)  
##  __См. также
#### Ссылки
[CardStoreAsyncResponse - ](T_Tessa_Cards_CardStoreAsyncResponse.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
