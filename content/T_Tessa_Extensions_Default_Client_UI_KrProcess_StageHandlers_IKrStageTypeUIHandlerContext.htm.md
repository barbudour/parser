# IKrStageTypeUIHandlerContext - интерфейс
Контекст расширений
[IStageTypeUIHandler](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IStageTypeUIHandler.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers](N_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrStageTypeUIHandlerContext : IExtensionContext
VB __Копировать
     Public Interface IKrStageTypeUIHandlerContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IKrStageTypeUIHandlerContext : IExtensionContext
F# __Копировать
     type IKrStageTypeUIHandlerContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[Action](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_Action.htm)|
Действие со строкой
[Row](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_Row.htm)
или значение null, если выполняется валидация строки с параметрами этапа
([Validate(IKrStageTypeUIHandlerContext)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IStageTypeUIHandler_Validate.htm)).  
---|---  
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
[CardModel](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_CardModel.htm)|
Модель карточки, в которой расположена строка
[Row](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_Row.htm).  
[Control](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_Control.htm)|
Элемент управления, в рамках которого выполняется событие или значение null,
если выполняется валидация строки с параметрами этапа
([Validate(IKrStageTypeUIHandlerContext)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IStageTypeUIHandler_Validate.htm)).  
[Row](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_Row.htm)|
Строка карточки с параметрами этапа, с которой производится действие.  
[RowModel](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_RowModel.htm)|
Модель строки
[Row](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_Row.htm)
с параметрами этапа вместе с формой.  
[SettingsForms](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_SettingsForms.htm)|
Коллекция, содержащая формы из типа карточки настроек текущего этапа.  
[StageTypeID](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_StageTypeID.htm)|
Идентификатор типа этапа.  
[ValidationResult](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_ValidationResult.htm)|  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers - пространство
имён](N_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers.htm)
