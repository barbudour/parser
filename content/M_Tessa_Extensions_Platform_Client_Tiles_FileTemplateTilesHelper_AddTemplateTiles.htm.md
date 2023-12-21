# FileTemplateTilesHelper.AddTemplateTiles - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Tiles](N_Tessa_Extensions_Platform_Client_Tiles.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static void AddTemplateTiles(
    	FileTemplateType templateType,
    	ITile parentTile,
    	IIconContainer iconContainer,
    	IUIContext uiContext,
    	Action<Guid, string> createFileTemplateAction
    )
VB __Копировать
     Public Shared Sub AddTemplateTiles ( 
    	templateType As FileTemplateType,
    	parentTile As ITile,
    	iconContainer As IIconContainer,
    	uiContext As IUIContext,
    	createFileTemplateAction As Action(Of Guid, String)
    )
C++ __Копировать
     public:
    static void AddTemplateTiles(
    	FileTemplateType templateType, 
    	ITile^ parentTile, 
    	IIconContainer^ iconContainer, 
    	IUIContext^ uiContext, 
    	Action<Guid, String^>^ createFileTemplateAction
    )
F# __Копировать
     static member AddTemplateTiles : 
            templateType : FileTemplateType * 
            parentTile : ITile * 
            iconContainer : IIconContainer * 
            uiContext : IUIContext * 
            createFileTemplateAction : Action<Guid, string> -> unit 
#### Параметры
templateType
[FileTemplateType](T_Tessa_Extensions_Platform_Shared_Cards_FileTemplateType.htm)
parentTile [ITile](T_Tessa_UI_Tiles_ITile.htm)
iconContainer [IIconContainer](T_Tessa_UI_IIconContainer.htm)
uiContext [IUIContext](T_Tessa_UI_IUIContext.htm)
createFileTemplateAction
[Action](https://learn.microsoft.com/dotnet/api/system.action-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[String](https://learn.microsoft.com/dotnet/api/system.string)>
## __См. также
#### Ссылки
[FileTemplateTilesHelper -
](T_Tessa_Extensions_Platform_Client_Tiles_FileTemplateTilesHelper.htm)
[Tessa.Extensions.Platform.Client.Tiles - пространство
имён](N_Tessa_Extensions_Platform_Client_Tiles.htm)
