# CardTableViewControlViewModel - конструктор
Инициализирует новый экземпляр класса
[CardTableViewControlViewModel](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTableViewControlViewModel(
    	CardTypeControl control,
    	ICardModel model,
    	ICardEditorModel cardEditor,
    	ICardUIResolver cardUIResolver,
    	ICardValidationManager validationManager,
    	CardParametersMapper parametersMapper,
    	CardTypeTableControl tableControl,
    	ISerializableObject extensionSettings
    )
VB __Копировать
     Public Sub New ( 
    	control As CardTypeControl,
    	model As ICardModel,
    	cardEditor As ICardEditorModel,
    	cardUIResolver As ICardUIResolver,
    	validationManager As ICardValidationManager,
    	parametersMapper As CardParametersMapper,
    	tableControl As CardTypeTableControl,
    	extensionSettings As ISerializableObject
    )
C++ __Копировать
     public:
    CardTableViewControlViewModel(
    	CardTypeControl^ control, 
    	ICardModel^ model, 
    	ICardEditorModel^ cardEditor, 
    	ICardUIResolver^ cardUIResolver, 
    	ICardValidationManager^ validationManager, 
    	CardParametersMapper^ parametersMapper, 
    	CardTypeTableControl^ tableControl, 
    	ISerializableObject^ extensionSettings
    )
F# __Копировать
     new : 
            control : CardTypeControl * 
            model : ICardModel * 
            cardEditor : ICardEditorModel * 
            cardUIResolver : ICardUIResolver * 
            validationManager : ICardValidationManager * 
            parametersMapper : CardParametersMapper * 
            tableControl : CardTypeTableControl * 
            extensionSettings : ISerializableObject -> CardTableViewControlViewModel
#### Параметры
control [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)
model [ICardModel](T_Tessa_UI_Cards_ICardModel.htm)
cardEditor [ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm)
cardUIResolver [ICardUIResolver](T_Tessa_UI_Cards_ICardUIResolver.htm)
validationManager
[ICardValidationManager](T_Tessa_Cards_Validation_ICardValidationManager.htm)
parametersMapper
[CardParametersMapper](T_Tessa_UI_Cards_Controls_CardParametersMapper.htm)
tableControl [CardTypeTableControl](T_Tessa_Cards_CardTypeTableControl.htm)
extensionSettings
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
## __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
