# Tessa.UI.Tiles.Extensions - пространство имён
Расширения для плиток.
##  __Классы
[TileAnyPanelLocationPolicy](T_Tessa_UI_Tiles_Extensions_TileAnyPanelLocationPolicy.htm)|
Политика, определяющая допустимость любого местоположения боковой панели для
выполнения методов расширения. Может быть использована для замещения другой
политики
[ITilePanelLocationPolicy](T_Tessa_UI_Tiles_Extensions_ITilePanelLocationPolicy.htm).  
---|---  
[TileExtension](T_Tessa_UI_Tiles_Extensions_TileExtension.htm)|  Базовый класс
для расширений, взаимодействующих с плитками.  
[TileGlobalExtensionContext](T_Tessa_UI_Tiles_Extensions_TileGlobalExtensionContext.htm)|
Контекст расширений для инициализации глобальной рабочей области с панелями
плиток.  
[TileLocalExtensionContext](T_Tessa_UI_Tiles_Extensions_TileLocalExtensionContext.htm)|
Контекст расширений для инициализации и финализации локальной рабочей области
с панелями плиток.  
[TilePanelExtensionContext](T_Tessa_UI_Tiles_Extensions_TilePanelExtensionContext.htm)|
Контекст расширений для управления отображением панели с плитками в локальной
рабочей области.  
[TilePanelFilterPolicy](T_Tessa_UI_Tiles_Extensions_TilePanelFilterPolicy.htm)|
Политика фильтрации расширений, использующая политику
[ITilePanelLocationPolicy](T_Tessa_UI_Tiles_Extensions_ITilePanelLocationPolicy.htm)
для того, чтобы не выполнять методы расширений, для которых в контексте
[ITilePanelExtensionContext](T_Tessa_UI_Tiles_Extensions_ITilePanelExtensionContext.htm)
использовано местоположение боковой панели, запрещённое указанной политикой.
Если политика
[ITilePanelLocationPolicy](T_Tessa_UI_Tiles_Extensions_ITilePanelLocationPolicy.htm)
не зарегистрирована, то метод расширения выполняется.  
[TilePanelLocationPolicy](T_Tessa_UI_Tiles_Extensions_TilePanelLocationPolicy.htm)|
Политика, определяющая допустимость местоположения боковой панели для
выполнения методов расширения.  
## __Интерфейсы
[ITileGlobalExtension](T_Tessa_UI_Tiles_Extensions_ITileGlobalExtension.htm)|
Расширение, выполняющее инициализацию для глобальной рабочей области с
плитками.  
---|---  
[ITileGlobalExtensionContext](T_Tessa_UI_Tiles_Extensions_ITileGlobalExtensionContext.htm)|
Контекст расширений для инициализации глобальной рабочей области с панелями
плиток.  
[ITileLocalExtension](T_Tessa_UI_Tiles_Extensions_ITileLocalExtension.htm)|
Расширение, выполняющее инициализацию и финализацию для локальной рабочей
области с плитками.  
[ITileLocalExtensionContext](T_Tessa_UI_Tiles_Extensions_ITileLocalExtensionContext.htm)|
Контекст расширений для инициализации и финализации локальной рабочей области
с панелями плиток.  
[ITilePanelExtension](T_Tessa_UI_Tiles_Extensions_ITilePanelExtension.htm)|
Расширение, выполняющее действия перед открытием и после закрытия левой или
правой боковой панели с плитками.  
[ITilePanelExtensionContext](T_Tessa_UI_Tiles_Extensions_ITilePanelExtensionContext.htm)|
Контекст расширений для управления отображением панели с плитками в локальной
рабочей области.  
[ITilePanelLocationPolicy](T_Tessa_UI_Tiles_Extensions_ITilePanelLocationPolicy.htm)|
Политика, определяющая допустимость местоположения боковой панели для
выполнения методов расширения.
