# OpenInModalDialogOnDoubleClickExtension.Clone - метод
Вызывается при клонировании модели source в контексте context
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public void Clone(
    	IWorkplaceViewComponent source,
    	IWorkplaceViewComponent cloned,
    	ICloneableContext context
    )
VB __Копировать
     Public Sub Clone ( 
    	source As IWorkplaceViewComponent,
    	cloned As IWorkplaceViewComponent,
    	context As ICloneableContext
    )
C++ __Копировать
     public:
    virtual void Clone(
    	IWorkplaceViewComponent^ source, 
    	IWorkplaceViewComponent^ cloned, 
    	ICloneableContext^ context
    ) sealed
F# __Копировать
     abstract Clone : 
            source : IWorkplaceViewComponent * 
            cloned : IWorkplaceViewComponent * 
            context : ICloneableContext -> unit 
    override Clone : 
            source : IWorkplaceViewComponent * 
            cloned : IWorkplaceViewComponent * 
            context : ICloneableContext -> unit 
#### Параметры
source [IWorkplaceViewComponent](T_Tessa_UI_Views_IWorkplaceViewComponent.htm)
     Исходная модель 
cloned [IWorkplaceViewComponent](T_Tessa_UI_Views_IWorkplaceViewComponent.htm)
     Клонированная модель 
context [ICloneableContext](T_Tessa_UI_Views_ICloneableContext.htm)
     Контекст клонирования 
#### Реализации
[IWorkplaceExtension<TModel>.Clone(TModel, TModel,
ICloneableContext)](M_Tessa_UI_Views_Extensions_IWorkplaceExtension_1_Clone.htm)  
##  __См. также
#### Ссылки
[OpenInModalDialogOnDoubleClickExtension -
](T_Tessa_Extensions_Platform_Client_Cards_OpenInModalDialogOnDoubleClickExtension.htm)
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
