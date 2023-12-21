# IRegistratorMetadata - свойства
##  __Свойства
[Description](P_Tessa_Extensions_IRegistratorMetadata_Description.htm)|
Описание регистратора. Не используется платформой, но может предоставляться в
информативных целях.  
---|---  
[IsPlatform](P_Tessa_Extensions_IRegistratorMetadata_IsPlatform.htm)|  Признак
того, что объект выполняет регистрацию платформенных расширений. Этот признак
используется системой, не рекомендуется его устанавливать.  
[Order](P_Tessa_Extensions_IRegistratorMetadata_Order.htm)|  Порядок
выполнения регистратора внутри этапа
[Tessa.Extensions.IRegistratorMetadata.Order].  
[Stage](P_Tessa_Extensions_IRegistratorMetadata_Stage.htm)| Этап выполнения
регистратора в цепочке регистрации.  
[Tag](P_Tessa_Extensions_IRegistratorMetadata_Tag.htm)|  Флаговое перечисление
с тегами регистратора, которые ограничивают область его использования. По
умолчанию используются теги [Tessa.Extensions.RegistratorTag.Default].  
[Type](P_Tessa_Extensions_IRegistratorMetadata_Type.htm)|  Тип сессии, для
которой будет выполняться регистратор, или
[Tessa.Platform.Runtime.SessionType.Unknown], если регистратор выполняется для
любого типа сессии и на клиенте, и на сервере (по умолчанию). Значение,
отличное от [Tessa.Platform.Runtime.SessionType.Unknown], актуально только для
сборок, которые могут сканироваться на наличие регистраторов и на клиенте, и
на сервере.  
## __См. также
#### Ссылки
[IRegistratorMetadata - ](T_Tessa_Extensions_IRegistratorMetadata.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
