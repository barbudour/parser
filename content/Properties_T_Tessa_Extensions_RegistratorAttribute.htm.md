# RegistratorAttribute - свойства
##  __Свойства
[Description](P_Tessa_Extensions_RegistratorAttribute_Description.htm)|
Описание регистратора. Не используется платформой, но может предоставляться в
информативных целях.  
---|---  
[IsPlatform](P_Tessa_Extensions_RegistratorAttribute_IsPlatform.htm)|  Признак
того, что объект выполняет регистрацию платформенных расширений. Этот признак
используется системой, не рекомендуется его устанавливать.  
[Order](P_Tessa_Extensions_RegistratorAttribute_Order.htm)|  Порядок
выполнения регистратора внутри этапа
[Tessa.Extensions.IRegistratorMetadata.Order].  
[Stage](P_Tessa_Extensions_RegistratorAttribute_Stage.htm)| Этап выполнения
регистратора в цепочке регистрации.  
[Tag](P_Tessa_Extensions_RegistratorAttribute_Tag.htm)|  Флаговое перечисление
с тегами регистратора, которые ограничивают область его использования. По
умолчанию используются теги [Tessa.Extensions.RegistratorTag.Default].  
[Type](P_Tessa_Extensions_RegistratorAttribute_Type.htm)|  Тип сессии, для
которой будет выполняться регистратор, или
[Tessa.Platform.Runtime.SessionType.Unknown], если регистратор выполняется для
любого типа сессии и на клиенте, и на сервере (по умолчанию). Значение,
отличное от [Tessa.Platform.Runtime.SessionType.Unknown], актуально только для
сборок, которые могут сканироваться на наличие регистраторов и на клиенте, и
на сервере.  
[TypeId](https://learn.microsoft.com/dotnet/api/system.attribute.typeid#system-
attribute-typeid)| When implemented in a derived class, gets a unique
identifier for this
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute).  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
##  __См. также
#### Ссылки
[RegistratorAttribute - ](T_Tessa_Extensions_RegistratorAttribute.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
