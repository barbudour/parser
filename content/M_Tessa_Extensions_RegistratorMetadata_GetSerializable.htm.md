# RegistratorMetadata.GetSerializable - метод
Возвращает метаинформацию, которая может быть сериализована через атрибут
[System.SerializableAttribute]. Если текущий объект уже сериализуется, то он
может вернуть себя же.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IRegistratorMetadata GetSerializable()
VB __Копировать
     Public Function GetSerializable As IRegistratorMetadata
C++ __Копировать
     public:
    virtual IRegistratorMetadata^ GetSerializable() sealed
F# __Копировать
     abstract GetSerializable : unit -> IRegistratorMetadata 
    override GetSerializable : unit -> IRegistratorMetadata 
#### Возвращаемое значение
[IRegistratorMetadata](T_Tessa_Extensions_IRegistratorMetadata.htm)  
Метаинформация, которая может быть сериализована.
#### Реализации
[ISerializableMetadata<TMetadata>.GetSerializable()](M_Tessa_Platform_Composition_ISerializableMetadata_1_GetSerializable.htm)  
##  __См. также
#### Ссылки
[RegistratorMetadata - ](T_Tessa_Extensions_RegistratorMetadata.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
