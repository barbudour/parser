# ExtensionTileHelper.CreateMoreTileIfNecessary - метод
Создаёт плитку "ещё", в которую добавляет все остальные плитки. Используется
для группировки типов создаваемых карточек. Возвращает признак того, что
плитка "ещё" была создана.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Tiles](N_Tessa_Extensions_Platform_Client_Tiles.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool CreateMoreTileIfNecessary(
    	int maxTilesBeforeAddingSubgroup,
    	ITileContextSource contextSource,
    	ref int tileOrder,
    	ref TileCollection tileCollection
    )
VB __Копировать
     Public Shared Function CreateMoreTileIfNecessary ( 
    	maxTilesBeforeAddingSubgroup As Integer,
    	contextSource As ITileContextSource,
    	ByRef tileOrder As Integer,
    	ByRef tileCollection As TileCollection
    ) As Boolean
C++ __Копировать
     public:
    static bool CreateMoreTileIfNecessary(
    	int maxTilesBeforeAddingSubgroup, 
    	ITileContextSource^ contextSource, 
    	int% tileOrder, 
    	TileCollection^% tileCollection
    )
F# __Копировать
     static member CreateMoreTileIfNecessary : 
            maxTilesBeforeAddingSubgroup : int * 
            contextSource : ITileContextSource * 
            tileOrder : int byref * 
            tileCollection : TileCollection byref -> bool 
#### Параметры
maxTilesBeforeAddingSubgroup
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
     Максимальное количество плиток, которое допустимо перед тем, как будет добавлена плитка "ещё". 
contextSource [ITileContextSource](T_Tessa_UI_Tiles_ITileContextSource.htm)
     Источник контекста для создаваемой плитки. Например, родительская плитка или боковая панель, в которую плитка добавлятся. 
tileOrder [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Отсчитываемый от нуля порядковый номер плитки в коллекции плиток.
tileCollection [TileCollection](T_Tessa_UI_Tiles_TileCollection.htm)
     Коллекция плиток, в которую выполняется добавление. После создания плитки "ещё" добавление должно производится в коллекцию дочерних плиток для "ещё". 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если плитка "ещё" была создана; false в противном случае.
## __См. также
#### Ссылки
[ExtensionTileHelper -
](T_Tessa_Extensions_Platform_Client_Tiles_ExtensionTileHelper.htm)
[Tessa.Extensions.Platform.Client.Tiles - пространство
имён](N_Tessa_Extensions_Platform_Client_Tiles.htm)
