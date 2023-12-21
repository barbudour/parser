# NumberDirectorContainer.Register - метод
Регистрирует зависимости API номеров для всех типов карточек по умолчанию или
для типа карточки с указанным идентификатором.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public INumberDirectorContainer Register(
    	Guid? typeID = null,
    	Func<IUnityContainer, INumberDirector> getDirectorFunc = null,
    	Func<IUnityContainer, INumberComposer> getComposerFunc = null,
    	Func<IUnityContainer, INumberQueueProcessor> getQueueProcessorFunc = null
    )
VB __Копировать
     Public Function Register ( 
    	Optional typeID As Guid? = Nothing,
    	Optional getDirectorFunc As Func(Of IUnityContainer, INumberDirector) = Nothing,
    	Optional getComposerFunc As Func(Of IUnityContainer, INumberComposer) = Nothing,
    	Optional getQueueProcessorFunc As Func(Of IUnityContainer, INumberQueueProcessor) = Nothing
    ) As INumberDirectorContainer
C++ __Копировать
     public:
    virtual INumberDirectorContainer^ Register(
    	Nullable<Guid> typeID = nullptr, 
    	Func<IUnityContainer^, INumberDirector^>^ getDirectorFunc = nullptr, 
    	Func<IUnityContainer^, INumberComposer^>^ getComposerFunc = nullptr, 
    	Func<IUnityContainer^, INumberQueueProcessor^>^ getQueueProcessorFunc = nullptr
    ) sealed
F# __Копировать
     abstract Register : 
            ?typeID : Nullable<Guid> * 
            ?getDirectorFunc : Func<IUnityContainer, INumberDirector> * 
            ?getComposerFunc : Func<IUnityContainer, INumberComposer> * 
            ?getQueueProcessorFunc : Func<IUnityContainer, INumberQueueProcessor> 
    (* Defaults:
            let _typeID = defaultArg typeID null
            let _getDirectorFunc = defaultArg getDirectorFunc null
            let _getComposerFunc = defaultArg getComposerFunc null
            let _getQueueProcessorFunc = defaultArg getQueueProcessorFunc null
    *)
    -> INumberDirectorContainer 
    override Register : 
            ?typeID : Nullable<Guid> * 
            ?getDirectorFunc : Func<IUnityContainer, INumberDirector> * 
            ?getComposerFunc : Func<IUnityContainer, INumberComposer> * 
            ?getQueueProcessorFunc : Func<IUnityContainer, INumberQueueProcessor> 
    (* Defaults:
            let _typeID = defaultArg typeID null
            let _getDirectorFunc = defaultArg getDirectorFunc null
            let _getComposerFunc = defaultArg getComposerFunc null
            let _getQueueProcessorFunc = defaultArg getQueueProcessorFunc null
    *)
    -> INumberDirectorContainer 
#### Параметры
typeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Идентификатор типа карточки, для которого выполняется регистрация, или null, если выполняется регистрация значения по умолчанию для всех типов для всех типов. 
getDirectorFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<IUnityContainer,
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm)> (Optional)
     Функция, выполняющая резолв объекта [INumberDirector] (предположительно из заданного контейнера). Возвращённый единожды экземпляр будет сохранён для последующего использования. Если равно null и регистрация выполняется для всех типов, то сохраняет предыдущую реализацию объекта. Если регистрация указывается для заданного типа, то при указании null задействует значение из регистрации по умолчанию. 
getComposerFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<IUnityContainer,
[INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm)> (Optional)
     Функция, выполняющая резолв объекта [INumberComposer] (предположительно из заданного контейнера). Возвращённый единожды экземпляр будет сохранён для последующего использования. Если равно null и регистрация выполняется для всех типов, то сохраняет предыдущую реализацию объекта. Если регистрация указывается для заданного типа, то при указании null задействует значение из регистрации по умолчанию. 
getQueueProcessorFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<IUnityContainer,
[INumberQueueProcessor](T_Tessa_Cards_Numbers_INumberQueueProcessor.htm)>
(Optional)
     Функция, выполняющая резолв объекта [INumberQueueProcessor] (предположительно из заданного контейнера). Возвращённый единожды экземпляр будет сохранён для последующего использования. Если равно null и регистрация выполняется для всех типов, то сохраняет предыдущую реализацию объекта. Если регистрация указывается для заданного типа, то при указании null задействует значение из регистрации по умолчанию. 
#### Возвращаемое значение
[INumberDirectorContainer](T_Tessa_Cards_Numbers_INumberDirectorContainer.htm)  
Текущий объект для цепочки вызовов.
#### Реализации
[INumberDirectorContainer.Register(Nullable<Guid>, Func<IUnityContainer,
INumberDirector>, Func<IUnityContainer, INumberComposer>,
Func<IUnityContainer,
INumberQueueProcessor>)](M_Tessa_Cards_Numbers_INumberDirectorContainer_Register.htm)  
##  __См. также
#### Ссылки
[NumberDirectorContainer -
](T_Tessa_Cards_Numbers_NumberDirectorContainer.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
