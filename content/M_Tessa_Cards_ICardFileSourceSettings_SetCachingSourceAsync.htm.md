# ICardFileSourceSettings.SetCachingSourceAsync - метод
Устанавливает источник получения настроек по местоположению файлов.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task SetCachingSourceAsync(
    	Func<ICardCache> getCardCacheFunc,
    	ILicenseManager licenseManager = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function SetCachingSourceAsync ( 
    	getCardCacheFunc As Func(Of ICardCache),
    	Optional licenseManager As ILicenseManager = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ SetCachingSourceAsync(
    	Func<ICardCache^>^ getCardCacheFunc, 
    	ILicenseManager^ licenseManager = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SetCachingSourceAsync : 
            getCardCacheFunc : Func<ICardCache> * 
            ?licenseManager : ILicenseManager * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _licenseManager = defaultArg licenseManager null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
getCardCacheFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)>
     Функция, возвращающая кэш с карточками и дополнительными настройками. Может быть равна null. Рекомендуется, чтобы функция всегда возвращала один и тот же экземпляр кэша. В связи с особенностями инициализации системы, в метод передаётся функция, а не конкретный экземпляр, чтобы на момент установки объект мог не инициализировать все свои зависимости. 
licenseManager
[ILicenseManager](T_Tessa_Platform_Licensing_ILicenseManager.htm) (Optional)
     Объект, предоставляющий информацию по текущей лицензии для ограничения файловых источников или null, если связь с лицензией не выполняется. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[ICardFileSourceSettings - ](T_Tessa_Cards_ICardFileSourceSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
