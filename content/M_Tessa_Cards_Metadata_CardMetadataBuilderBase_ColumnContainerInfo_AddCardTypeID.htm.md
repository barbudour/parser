# CardMetadataBuilderBase.ColumnContainerInfo.AddCardTypeID - метод
Добавляет информацию о том, что текущая колонка используется в типе карточки с
заданным идентификатором.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void AddCardTypeID(
    	Guid id
    )
VB __Копировать
     Public Sub AddCardTypeID ( 
    	id As Guid
    )
C++ __Копировать
     public:
    void AddCardTypeID(
    	Guid id
    )
F# __Копировать
     member AddCardTypeID : 
            id : Guid -> unit 
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор типа карточки, в котором используется текущая колонка. Для успешного использования добавленной информации заданный один и тот же идентификатор типа карточки не должен быть задан несколько раз для одной и той же колонки. 
## __См. также
#### Ссылки
[CardMetadataBuilderBase.ColumnContainerInfo -
](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
