# ExtensionTileHelper.RegroupAndAddMoreIfNecessary - метод
В заданной коллекции и во всех дочерних коллекциях добавляет подгруппу "ещё",
если количество отображаемых плиток превышает maxTiles.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Tiles](N_Tessa_Extensions_Platform_Client_Tiles.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static void RegroupAndAddMoreIfNecessary(
    	TileCollection tiles,
    	ITileContextSource contextSource,
    	int maxTiles
    )
VB __Копировать
     Public Shared Sub RegroupAndAddMoreIfNecessary ( 
    	tiles As TileCollection,
    	contextSource As ITileContextSource,
    	maxTiles As Integer
    )
C++ __Копировать
     public:
    static void RegroupAndAddMoreIfNecessary(
    	TileCollection^ tiles, 
    	ITileContextSource^ contextSource, 
    	int maxTiles
    )
F# __Копировать
     static member RegroupAndAddMoreIfNecessary : 
            tiles : TileCollection * 
            contextSource : ITileContextSource * 
            maxTiles : int -> unit 
#### Параметры
tiles [TileCollection](T_Tessa_UI_Tiles_TileCollection.htm)
    Коллекция плиток, которую необходимо сгруппировать с учётом подгруппы "ещё".
contextSource [ITileContextSource](T_Tessa_UI_Tiles_ITileContextSource.htm)
    Источник контекста для плитки "ещё".
maxTiles [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
     Максимальное количество плиток на одном уровне для плиток в коллекции maxTiles, с учётом дочерних коллекций. 
## __См. также
#### Ссылки
[ExtensionTileHelper -
](T_Tessa_Extensions_Platform_Client_Tiles_ExtensionTileHelper.htm)
[Tessa.Extensions.Platform.Client.Tiles - пространство
имён](N_Tessa_Extensions_Platform_Client_Tiles.htm)
