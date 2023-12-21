# IRegistratorMetadata - интерфейс
Метаинформация по атрибуту
[RegistratorAttribute](T_Tessa_Extensions_RegistratorAttribute.htm).
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IRegistratorMetadata : ISerializableMetadata<IRegistratorMetadata>
VB __Копировать
     Public Interface IRegistratorMetadata
    	Inherits ISerializableMetadata(Of IRegistratorMetadata)
C++ __Копировать
     public interface class IRegistratorMetadata : ISerializableMetadata<IRegistratorMetadata^>
F# __Копировать
     type IRegistratorMetadata = 
        interface
            interface ISerializableMetadata<IRegistratorMetadata>
        end
Implements
    [ISerializableMetadata](T_Tessa_Platform_Composition_ISerializableMetadata_1.htm)<IRegistratorMetadata>
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
## __Методы
[GetSerializable](M_Tessa_Platform_Composition_ISerializableMetadata_1_GetSerializable.htm)|
Возвращает метаинформацию, которая может быть сериализована через атрибут
[System.SerializableAttribute]. Если текущий объект уже сериализуется, то он
может вернуть себя же.  
(Унаследован от
[ISerializableMetadata<TMetadata>](T_Tessa_Platform_Composition_ISerializableMetadata_1.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
