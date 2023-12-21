# CardMetadataHelper.GetDefaultValueFunc - метод
Возвращает функцию, которая для заданного режима создания карточки получает
значение по умолчанию для указанной в параметре колонки
[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Func<CardMetadataColumn, Object> GetDefaultValueFunc(
    	CardNewMode mode
    )
VB __Копировать
     Public Shared Function GetDefaultValueFunc ( 
    	mode As CardNewMode
    ) As Func(Of CardMetadataColumn, Object)
C++ __Копировать
     public:
    static Func<CardMetadataColumn^, Object^>^ GetDefaultValueFunc(
    	CardNewMode mode
    )
F# __Копировать
     static member GetDefaultValueFunc : 
            mode : CardNewMode -> Func<CardMetadataColumn, Object> 
#### Параметры
mode [CardNewMode](T_Tessa_Cards_CardNewMode.htm)
    Режим создания карточки, определяющий способ заполнения значений.
#### Возвращаемое значение
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>  
Функция, которая для заданного режима создания карточки получает значение по
умолчанию для указанной в параметре колонки
[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm).
## __См. также
#### Ссылки
[CardMetadataHelper - ](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
