# CardMetadataHelper.HasLength15 - метод
Возвращает признак того, что заданный тип имеет длину, которая умещается в 15
бит и может быть сериализована как 16-битное знаковое число.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool HasLength15(
    	CardMetadataRuntimeType type
    )
VB __Копировать
     Public Shared Function HasLength15 ( 
    	type As CardMetadataRuntimeType
    ) As Boolean
C++ __Копировать
     public:
    static bool HasLength15(
    	CardMetadataRuntimeType type
    )
F# __Копировать
     static member HasLength15 : 
            type : CardMetadataRuntimeType -> bool 
#### Параметры
type
[CardMetadataRuntimeType](T_Tessa_Cards_Metadata_CardMetadataRuntimeType.htm)
    Тип данных, который может разместить данные карточки заданным образом.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданный тип имеет длину, которая умещается в 16 бит; false в
противном случае.
## __См. также
#### Ссылки
[CardMetadataHelper - ](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
