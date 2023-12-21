# CardCacheSettingsProxy.InvalidateSourceAsync(String, CancellationToken) -
метод
Выполняет удаление настройки из кэша по заданному ключу.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InvalidateSourceAsync(
    	string key,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function InvalidateSourceAsync ( 
    	key As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ InvalidateSourceAsync(
    	String^ key, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member InvalidateSourceAsync : 
            key : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, для которого требуется удалить настройку из кэша.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __Заметки
Метод выполняет сброс кэша для декорируемого объекта.
## __Исключения
[System.ArgumentNullException]|  Аргумент key равен null.  
---|---  
[System.ArgumentOutOfRangeException]|  Аргумент key содержит строку, имеющую
большую длину, чем максимально допустимая длина
[Tessa.Cards.Caching.CardCacheHelper.MaxKeyLength].  
## __См. также
#### Ссылки
[CardCacheSettingsProxy - ](T_Tessa_Cards_Caching_CardCacheSettingsProxy.htm)
[InvalidateSourceAsync -
перегрузка](Overload_Tessa_Cards_Caching_CardCacheSettingsProxy_InvalidateSourceAsync.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
