# CardMetadataHelper.Convert - метод
Преобразует объект в заданный тип, обеспечивающий возможность хранения объекта
в карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Object Convert(
    	Object value,
    	CardMetadataRuntimeType targetType
    )
VB __Копировать
     Public Shared Function Convert ( 
    	value As Object,
    	targetType As CardMetadataRuntimeType
    ) As Object
C++ __Копировать
     public:
    static Object^ Convert(
    	Object^ value, 
    	CardMetadataRuntimeType targetType
    )
F# __Копировать
     static member Convert : 
            value : Object * 
            targetType : CardMetadataRuntimeType -> Object 
#### Параметры
value [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Объект, значение которого требуется преобразовать в заданный тип.
targetType
[CardMetadataRuntimeType](T_Tessa_Cards_Metadata_CardMetadataRuntimeType.htm)
    Целевой тип, обеспечивающий способ хранения заданного объекта в карточке.
#### Возвращаемое значение
[Object](https://learn.microsoft.com/dotnet/api/system.object)  
Заданный объект, преобразованный для хранения в карточке.
##  __См. также
#### Ссылки
[CardMetadataHelper - ](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
