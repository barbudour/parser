# KrToken - свойства
##  __Свойства
[CardID](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken_CardID.htm)|
Идентификатор карточки. Если равен
[Empty](https://learn.microsoft.com/dotnet/api/system.guid.empty), то
считается, что токен подписан для любой карточки, что актуально, прежде всего,
для алгоритма создания карточки cardRepository.New().  
---|---  
[CardVersion](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken_CardVersion.htm)|
Номер версии карточки. Если равен
[DoNotCheckVersion](F_Tessa_Cards_ComponentModel_CardComponentHelper_DoNotCheckVersion.htm),
то считается, что токен подписан для любой версии карточки.  
[ExpiryDate](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken_ExpiryDate.htm)|
Дата и время истечения токена.  
[ExtendedCardSettings](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken_ExtendedCardSettings.htm)|
Настройки доступа к карточке по секциям  
[Info](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken_Info.htm)|
Дополнительная информация в токене безопасности. Должна быть записана до
подписи токена, иначе он будет считаться не валидным.  
[Permissions](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken_Permissions.htm)|
Права на карточку типового решения. Хранит список идентификаторов объектов
[KrPermissionFlagDescriptor](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor.htm)  
[PermissionsVersion](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken_PermissionsVersion.htm)|  
[Signature](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken_Signature.htm)|
Подпись токена, которая гарантирует его валидность. Подписываются все другие
поля, кроме собственно подписи.  
## __См. также
#### Ссылки
[KrToken - ](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
